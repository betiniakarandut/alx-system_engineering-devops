#!/usr/bin/python3
"""Module for hot post"""
import sys as s
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed for a given subreddit."""
    subreddit = s.argv[1]
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "SpyBot"}
    response = requests.get(url, headers=headers)
    
    if response.status_code >= 300:
        return None
    else:
       data = response.json()
       hotPost = data["data"]["children"]
       for index, hot in enumerate(hotPost, start=1):
           hots = hot["data"]["title"]
           print(hots)