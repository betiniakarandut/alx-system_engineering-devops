#!/usr/bin/python3
"""Module to find the number of subcribers on reddit"""
import requests
import sys as s


def number_of_subscribers(subreddit):
    """function that queries the Reddit API.
    
    Args:
        subreddit: str

    Return: number of subscribers
    """
    subreddit = s.argv[1]
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers={"User-Agent": "MyBot"})
    if response.status_code >= 300:
        return (0)
    else:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
