#!/usr/bin/python3
""" doc """

import requests


def recurse(subreddit, hot_list=[], after=None):
    """ doc """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    query = {'limit': 100, 'after': after}
    resp = requests.get(url, headers={'User-Agent': 'Haroldo'},
                        allow_redirects=False, params=query)
    if resp.status_code != 200:
        return None
    nxt = resp.json().get('data').get('after')
    if nxt is not None:
        recurse(subreddit, hot_list, nxt)
    objs = resp.json().get('data').get('children')
    for obj in objs:
        hot_list.append(obj.get('data').get('title'))
    return hot_list
