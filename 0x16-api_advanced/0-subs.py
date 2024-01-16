#!/usr/bin/env python3
"""
subscribers_fetcher.py - Retrieves the number of subscribers
for a specified subreddit using the Reddit API.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Retrieves and returns the number of subscribers for a given subreddit.
    If the subreddit is not valid or an error occurs, returns 0.
    """
    subreddit_url = f"https://www.reddit.com/r/{subreddit_name}/about.json"
    custom_headers = {"User-Agent": "my_custom_user_agent"}

    try:
        response = requests.get(subreddit_url, headers=custom_headers,
                                allow_redirects=False)
        if response.status_code == 200:
            subreddit_data = response.json()
            subscribers_count = subreddit_data['data']['subscribers']
            return subscribers_count
        else:
            return 0
    except Exception as error:
        print(f"Error: {error}")
        return 0
