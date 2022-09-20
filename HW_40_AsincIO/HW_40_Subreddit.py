import asyncio
import time
import httpx
from requests import get
import pprint


# Task 2
# Requests using asyncio and aiohttp
# Download all comments from a subreddit of your choice
# using URL: https://api.pushshift.io/reddit/comment/search/ .
# As a result, store all comments in chronological order in JSON and dump it
# to a file. For this task asyncio and aiohttp for making
# requests to reddit API.


def create_list_subreddits(url):
    data = get(url).json()
    list_subreddits = []
    for i in data['data']:
        list_subreddits.append((i['subreddit'], ))
    return list_subreddits


def create_subreddit_request(subreddit):
    subreddit_request = {}
    request = f'https://api.pushshift.io/reddit/comment/' \
              f'search?subreddit={subreddit[0]}'
    subreddit_request[subreddit] = request
    return subreddit_request

subreddit_response = {}

async def collect(subreddit_request):

    for key, value in subreddit_request.items():
        try:
            async with httpx.AsyncClient() as session:
                response = await session.get(value, timeout=10)
            subreddit_response[key[0]] = response.json()

        except Exception:
            print(key, value)


comments_by_subreddit = {}


def create_result(subreddit_response):
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


async def process(subreddit):
    subreddit_request = create_subreddit_request(subreddit)

    await collect(subreddit_request)

    create_result(subreddit_response)


async def main():

    url = 'https://api.pushshift.io/reddit/comment/search'

    list_subreddits = create_list_subreddits(url)

    tasks = []

    for subreddit in list_subreddits:
        task = asyncio.create_task(process(subreddit))
        tasks.append(task)

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    pprint.pprint(comments_by_subreddit)
    print(time.time() - t1)
