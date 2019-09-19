#!/usr/bin/python3
""" doc """

import requests


def recurse(subreddit, hot_list=[]):
    """ doc """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    query = {'limit': 100}
    resp = requests.get(url, headers={'User-Agent': 'Haroldo'},
                        allow_redirects=False, params=query)
    if resp.status_code == 200:
        objs = resp.json().get('data').get('children')
        for obj in objs:
            hot_list.append(obj.get('data').get('title'))
        nxt = resp.json().get('data').get('after')
        if nxt is not None:
            return recurse(subreddit, hot_list)
        else:
            return hot_list
    else:
        print("None")
