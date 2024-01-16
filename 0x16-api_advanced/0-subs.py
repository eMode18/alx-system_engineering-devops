#!/usr/bin/python3
"""
0-subs
"""
import requests


def number_of_subscribers(subreddit):
    subreddit_url = f'https://www.reddit.com/r/{subreddit}/about.json'
    subreddit_headers = {'User-Agent': 'MyBot/1.0'}
    try:
        response = requests.get(subreddit_url, headers=subreddit_headers,
                                allow_redirects=False)
        data = response.json()
        return data['data']['subscribers']
    except (requests.RequestException, KeyError):
        return 0


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
