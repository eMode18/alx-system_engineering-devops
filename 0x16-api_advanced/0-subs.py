#!/usr/bin/python3
"""Retrieve the subscriber count for a specific subreddit by querying the
Reddit API.

Args:
    subreddit (str): The name of the subreddit.

Returns:
    int: The number of subscribers for the specified subreddit, or 0 if the
    subreddit is not found or there is an issue with the API request.
"""
import requests


def number_of_subscribers(subreddit):
    """Retrieve the subscriber count for a specific subreddit by querying the
    Reddit API.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the specified subreddit, or 0 if the
        subreddit is not found or there is an issue with the API request.
    """
    api_link = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    res_headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(api_link, res_headers=res_headers)
    if response.status_code == 200:
        data = response.json()
        return data.get('data').get('subscribers')
    else:
        return 0
