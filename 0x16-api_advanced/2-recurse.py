#!/usr/bin/python3
"""
queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """
    returns a list containing the titles of all
    hot articles for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 25, 'after': after}
    headers = {'User-Agent': 'bot0'}

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        hot_list.extend(post['data']['title'] for post in posts)
        after = data['data']['after']

        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    return None
