#!/usr/bin/python3
"""
function that queries the Reddit API
and returns the number of subscribers
"""
from requests import get


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    res = get(url, headers={"User-Agent": "bot"})

    if res.status_code == 200:
        data = res.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
