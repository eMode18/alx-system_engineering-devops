#!/usr/bin/python3
"""
A utility to fetch subscriber count for specified Reddit communities.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Fetches and returns the subscriber count for a specific subreddit.
    Parameters:
    - subreddit (str): The subreddit for which to retrieve subscriber count.
    Returns:
    - int: The number of subscribers. Returns 0 if subreddit 
    is not found or on error.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "eMode18"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        response_data = response.json()
        sub_count = response_data['data']['subscribers']
        return sub_count
    else:
        return 0
