#!/usr/bin/env python3
"""
1-top_ten.py - Prints the titles of the first 10 hot posts
for a given subreddit using the Reddit API.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    If the subreddit is invalid, prints None.
    """
    endpoint_url = f"https://www.reddit.com/r/{subreddit_name}/hot.json"
    custom_headers = {"User-Agent": "my_custom_user_agent"}

    try:
        response = requests.get(endpoint_url, headers=custom_headers,
                                params={"limit": 10})

        if response.status_code == 200:
            response_data = response.json()
            posts = response_data['data']['children']

            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except Exception as error:
        print(f"Error: {error}")
