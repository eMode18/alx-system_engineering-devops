#!/usr/bin/python3
"""Retrieve and print the titles of the first 10 hot posts for a specified
subreddit by querying the Reddit API.

Args:
    subreddit (str): The name of the subreddit.

Prints:
    The titles of the first 10 hot posts for the specified subreddit, or
    "None" if there is an issue with the API request or no posts are found.
"""
import requests
import sys


def top_ten(subreddit):
    """Retrieve and print the titles of the first 10 hot posts for a specified
    subreddit by querying the Reddit API.

    Args:
        subreddit (str): The name of the subreddit.

    Prints:
        The titles of the first 10 hot posts for the specified subreddit, or
        "None" if there is an issue with the API request or no posts are found.
    """
    api_link = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res_headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(api_link, res_headers=res_headers,
                                allow_redirects=False)
        if response.status_code == 200:
            node = response.json().get('data').get('node')
            for i in range(10):
                print(node[i].get('data').get('title'))
        else:
            print("None")
    except Exception:
        print("None")
