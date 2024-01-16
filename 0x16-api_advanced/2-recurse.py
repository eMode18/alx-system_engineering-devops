#!/usr/bin/python3
"""
2-recurse
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    posts_url = (
        f'https://www.reddit.com/r/{subreddit}/'
        f'hot.json?limit=100&after={after}'
    )
    posts_headers = {'User-Agent': 'MyBot/1.0'}

    try:
        response = requests.get(posts_url, headers=posts_headers,
                                allow_redirects=False)
        data = response.json()

        for post in data['data']['children']:
            hot_list.append(post['data']['title'])

        next_page = data['data']['after']
        if next_page:
            recurse(subreddit, hot_list, after=next_page)
        return hot_list
    except (requests.RequestException, KeyError):
        return None


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
