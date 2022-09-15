import threading
import time
import json
from requests import get
from concurrent.futures import ThreadPoolExecutor
import pprint


# Task 1
# Make a class called Counter, and make it a subclass of the Thread class in
# the Threading module. Make the class have two global variables, one called
# counter set to 0, and another called rounds set to 100.000. Now implement
# the run() method, let it include a simple for-loop that iterates through
# rounds (e.i. 100.000 times) and for each time increments the value of the
# counter by 1. Create 2 instances of the thread and start them, then join them
# and check the result of the counter, it should be 200.000, right? Run it a
# couple of times and consider some different reasons why you get the answer
# that you get.


counter = 0
rounds = 100000


class Counter(threading.Thread):

    def run(self):
        global counter
        temp_counter = counter
        for _ in range(rounds):
            temp_counter += 1
        time.sleep(0.1)
        counter = temp_counter
        return counter

###############################################################################
# Task 2
# Requests using multiprocessing
# Download all comments from a subreddit of your choice
# using URL: https://api.pushshift.io/reddit/comment/search/ .
# As a result, store all comments in chronological order in JSON and dump it
# to a file. For this task use Threads for making requests to reddit API.


def create_list_subreddits(url):
    data = get(url).json()
    list_subreddits = []
    for i in data['data']:
        list_subreddits.append(i['subreddit'])
    return list_subreddits


def create_subreddit_request(list_subreddits):
    subreddit_request = {}
    for subreddit in list_subreddits:
        request = f'https://api.pushshift.io/reddit/comment/' \
                  f'search?subreddit={subreddit}'
        subreddit_request[subreddit] = request
    return subreddit_request


subreddit_response = {}


def collect(subreddit, request):
    global subreddit_response
    subreddit_response[subreddit] = get(request).json()
    return subreddit_response


def run_threads(subreddit_request):
    with ThreadPoolExecutor() as ex:
        for key, value in subreddit_request.items():
            ex.submit(collect, key, value)


def create_result(subreddit_response):
    comments_by_subreddit = {}
    for subreddit, response in subreddit_response.items():
        comment_by_author = {}
        for post in response['data']:
            author = post['author']
            comment = post['body']
            if author in comment_by_author.keys():
                comment_by_author[author].append(comment)
            else:
                comment_by_author[author] = [comment]
        comments_by_subreddit[subreddit] = comment_by_author
    return comments_by_subreddit


def main():
    # Task 1
    # count_1 = Counter()
    # count_2 = Counter()
    #
    # count_1.start()
    # count_2.start()
    #
    # count_1.join()
    # count_2.join()
    #
    # print(counter)
#########################################################################
    # Task 2
    url = 'https://api.pushshift.io/reddit/comment/search'

    list_subreddits = create_list_subreddits(url)
    subreddit_request = create_subreddit_request(list_subreddits)

    run_threads(subreddit_request)

    result = create_result(subreddit_response)
    pprint.pprint(result)


if __name__ == '__main__':
    main()