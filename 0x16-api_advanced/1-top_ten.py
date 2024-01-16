#!/usr/bin/python3
"""
1-top_ten
"""
import requests


def top_ten(subreddit):
    posts_url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    posts_headers = {'User-Agent': 'MyBot/1.0'}

    try:
        response = requests.get(posts_url, headers=posts_headers,
                                allow_redirects=False)
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    except (requests.RequestException, KeyError):
        print(None)


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
