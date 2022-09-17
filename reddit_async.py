import asyncio
import os
import aiohttp
from requests import get


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


async def collect(subreddit_request):
    subreddit_response = {}
    for key, value in subreddit_request.items():
        try:
            subreddit_response[key[0]] = await get(value).json()
        except Exception:
            print(key, value)
    print(subreddit_response)
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
    return comments_by_subreddit

res = []
def process(subreddit):
    subreddit_request = create_subreddit_request(subreddit)
    subreddit_response = collect(subreddit_request)
    comments_by_subreddit = create_result(subreddit_response)
    print('process executed', comments_by_subreddit)
    global res
    res.append(comments_by_subreddit)
    return comments_by_subreddit


async def main():

    url = 'https://api.pushshift.io/reddit/comment/search'

    list_subreddits = create_list_subreddits(url)

    tasks = []
    async with aiohttp.ClientSession():
        for i in list_subreddits:
            task = asyncio.create_task(process(i))
            tasks.append(task)

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
    print(res)