#!/usr/bin/python3
""" doc """

import requests


def top_ten(subreddit):
    """ doc """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    query = {'limit': 10}
    resp = requests.get(url, headers={'User-Agent': 'Haroldo'},
                        allow_redirects=False, params=query)
    if resp.status_code == 200:
        objs = resp.json().get('data').get('children')
        for obj in objs:
            print(obj.get('data').get('title'))
    else:
        print("None")
