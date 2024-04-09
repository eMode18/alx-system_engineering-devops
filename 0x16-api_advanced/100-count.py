#!/usr/bin/python3
"""
Recursive function to query the Reddit API, parse the titles of
all hot articles, and print a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Count occurrences of keywords in titles of hot articles in a subreddit.
    Args:
        subreddit (str): The name of the subreddit to search.
        word_list (list): List of keywords to count occurrences of.
        after (str, optional): Parameter used for pagination in Reddit API.
        counts (dict, optional): Dictionary to store keyword counts.

    Prints:
        Sorted count of keywords in descending order of occurrences.
    """
    if counts is None:
        counts = {}
    if not word_list:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word.lower()}: {count}")
        return
    if word_list:
        word = word_list.pop()
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        headers = {"User-Agent": "Mozilla/5.0"}
        params = {"limit": 100, "after": after}
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                title = post['data']['title']
                if word.lower() in title.lower().split():
                    counts[word.lower()] = counts.get(word.lower(), 0) + 1

            # Recursive call to count words with the remaining word_list
            after = data['data']['after']
            count_words(subreddit, word_list, after, counts)
        else:
            print("Invalid subreddit or no posts match.")
            return
