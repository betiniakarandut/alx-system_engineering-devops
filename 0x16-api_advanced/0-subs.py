#!/usr/bin/pyhton3
"""Module to find the number of subcribers on reddit"""

def def number_of_subscribers(subreddit):
    """function that queries the Reddit API.
    
    Args:
        subreddit: str

    Return: number of subscribers
    """
    import requests
    info = requests.get("https://www.reddit.com/r/{}/about.json"
                        .format(subreddit),
                        headers = {"User-Agent": "My-User-Agent"}.
                        allow_redirects=False)
    if info.status_code >= 300:
        return (0)
    return info/json().get("data").get("subscribers") 
