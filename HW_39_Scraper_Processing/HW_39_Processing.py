import concurrent
import multiprocessing
import os
import threading
import time
import json
from requests import get
from concurrent.futures import ThreadPoolExecutor
import pprint


# Task 2
# Requests using multiprocessing
# Download all comments from a subreddit of your choice
# using URL: https://api.pushshift.io/reddit/comment/search/ .
# As a result, store all comments in chronological order in JSON and dump it
# to a file. For this task use concurrent and multiprocessing for making
# requests to reddit API.


def create_list_subreddits(url):
    data = get(url).json()
    list_subreddits = []
    for i in data['data']:
        list_subreddits.append((i['subreddit'], ))
    # print(list_subreddits)
    return list_subreddits


def create_subreddit_request(subreddit):
    subreddit_request = {}
    request = f'https://api.pushshift.io/reddit/comment/' \
              f'search?subreddit={subreddit[0]}'
    subreddit_request[subreddit] = request
    # print(subreddit_request)
    return subreddit_request


def collect(subreddit_request):
    subreddit_response = {}
    for key, value in subreddit_request.items():
        try:
            subreddit_response[key[0]] = get(value).json()
        except:
            print(key, value)
    # print(subreddit_response)
    return subreddit_response


def create_result(subreddit_response):
    comments_by_subreddit = {}
    for subreddit, response in subreddit_response.items():
        comment_by_author = {}
        for post in response['data']:
            author = post.get('author')
            comment = post.get('body')
            if author in comment_by_author.keys():
                comment_by_author[author].append(comment)
            else:
                comment_by_author[author] = [comment]
        comments_by_subreddit[subreddit] = comment_by_author
    # print(comments_by_subreddit)
    return comments_by_subreddit

# qu = multiprocessing.Queue()

def process(subreddit):
    # global qu
    subreddit_request = create_subreddit_request(subreddit)
    subreddit_response = collect(subreddit_request)
    comments_by_subreddit = create_result(subreddit_response)
    # qu.put(comments_by_subreddit)
    # print(qu.qsize())
    print('process executed', os.getpid(), comments_by_subreddit)
    return comments_by_subreddit


def main():

    url = 'https://api.pushshift.io/reddit/comment/search'

    list_subreddits = create_list_subreddits(url)

    with multiprocessing.Pool(3) as p:
        pprint.pprint(p.map(process, list_subreddits))


    # p = multiprocessing.Pool(3)
    # it = p.imap(process, list_subreddits)
    # print(it.next())


    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     print(executor.map(process, list_subreddits))



    # processes = []
    # for i in list_subreddits:
    #     p = multiprocessing.Process(target=process, args=i)
    #     processes.append(p)
    #     p.start()


    # for proces in processes:
    #     proces.join()


if __name__ == '__main__':
    main()