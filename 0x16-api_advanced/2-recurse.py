#!/usr/bin/python3
"""Recursive module to querry reddit api"""


def recurse(subreddit, hot_list=[], count=0, after=None):
    """prints a sorted count of given keywords

    Args:
        subreddit: strn
        hot_list: list
        count: int

    Returns:
        recursively a list containing the titles of all hot articles
    """
    import requests

    res = requests.get("https://www.reddit.com/r/{}/hot.json"
                       .format(subreddit),
                       params={"count": count, "after": after},
                       headers={"User-Agent": "My-User-Agent"},
                       allow_redirects=False)
    if res.status_code >= 400:
        return None

    hot_l = hot_list + [child.get("data").get("title")
                        for child in res.json()
                        .get("data")
                        .get("children")]

    feedback = res.json()
    if not feedback.get("data").get("after"):
        return hot_l

    return recurse(subreddit, hot_l, feedback.get("data").get("count"),
                   feedback.get("data").get("after"))
