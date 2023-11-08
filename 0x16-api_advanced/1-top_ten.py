#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit.
"""
from requests import get


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot
    posts listed for a given subreddit
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    res = get(url, headers={"User-Agent": "bot"})

    if res.status_code == 200:
        data = res.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            print(title)
    else:
        print(None)
