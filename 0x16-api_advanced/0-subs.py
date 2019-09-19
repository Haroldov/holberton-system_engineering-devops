#!/usr/bin/python3
""" doc """

import requests


def number_of_subscribers(subreddit):
    """ doc """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    resp = requests.get(url, headers={'User-Agent': 'Haroldo'},
                        allow_redirects=False)
    if resp.status_code == 200:
        return resp.json().get('data').get('subscribers')
    else:
        return 0
