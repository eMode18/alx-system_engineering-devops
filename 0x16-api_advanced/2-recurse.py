#!/usr/bin/python3
"""Retrieve a list of titles for all hot articles in a specified subreddit
using a recursive function that queries the Reddit API.

Args:
    subreddit (str): The name of the subreddit.

Returns:
    list: A list containing the titles of all hot articles for the specified
    subreddit, or None if the subreddit is not found.
"""
import requests


def recurse(subreddit, hot_list=[], after_token="", post_count=0):
    """Retrieve a list of titles for all hot articles in a specified subreddit
    using a recursive function that queries the Reddit API.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of hot articles
        (default=[]).
        after_token (str): Token used for pagination (default="").
        post_count (int): Counter for the number of articles retrieved
        (default=0).

    Returns:
        list: A list containing the titles of all hot articles for the
        specified
        subreddit, or None if the subreddit is not found.
    """
    base_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    user_agent_headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    query_params = {
        "after": after_token,
        "count": post_count,
        "limit": 100
    }
    response = requests.get(base_url, headers=user_agent_headers,
                            params=query_params, allow_redirects=False)
    if response.status_code == 404:
        return None

    response_data = response.json().get("data")
    after_token = response_data.get("after")
    post_count += response_data.get("dist")
    for post_data in response_data.get("children"):
        hot_list.append(post_data.get("data").get("title"))

    if after_token is not None:
        return recurse(subreddit, hot_list, after_token, post_count)
    return hot_list
