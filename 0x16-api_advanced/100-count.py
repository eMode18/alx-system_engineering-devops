#!/usr/bin/python3
"""
Function to tally occurrences of specified words in titles of
hot posts of a Reddit subreddit.
"""
import requests


def count_words(subreddit, word_list, next_page=None, word_counts={}):
    """
    Recursively queries the Reddit API for hot posts, parses their titles,
    and prints a sorted count of specified keywords found in the titles.
    """
    if not word_list or not subreddit:
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    params = {"limit": 100}
    if next_page:
        params["after"] = next_page

    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    children = data["data"]["children"]

    for post in children:
        title = post["data"]["title"].lower()
        for word in word_list:
            if word.lower() in title:
                word_counts[word] = (
                    word_counts.get(word, 0) +
                    title.count(word.lower())
                )
    next_page = data["data"]["after"]
    if next_page:
        count_words(subreddit, word_list, next_page, word_counts)
    else:
        sorted_counts = sorted(word_counts.items(),
                               key=lambda x: (-x[1], x[0].lower()))
        for word, count in sorted_counts:
            print("{}: {}".format(word.lower(), count))
