#!/usr/bin/python3
import requests


def recurse(subreddit_name, post_list=[], after=None):
    """
    Recursively queries the Reddit API and retrieves a list of titles for
    all hot articles in the specified subreddit.
    Returns None if the subreddit is invalid or no results are found.
    """
    subreddit_url = f"https://www.reddit.com/r/{subreddit_name}/hot.json"

    request_headers = {'User-agent': 'my-bot'}
    request_params = {'after': after} if after else {}

    try:
        api_response = requests.get(subreddit_url, headers=request_headers,
                                    params=request_params,
                                    allow_redirects=False)

        if api_response.status_code == 200:
            response_data = api_response.json().get('data')
            after = response_data.get('after')
            posts = response_data.get('children')

            post_list.extend([post.get("data").get("title") for post in posts])

            if after is not None:
                return recurse(subreddit_name, post_list, after)
            else:
                return post_list if post_list else None
        else:
            return None
    except Exception as error:
        print(f"Error: {error}")
        return None
