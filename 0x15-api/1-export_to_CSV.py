#!/usr/bin/python3
""" doc """

import csv
import requests
from sys import argv

if __name__ == "__main__" and len(argv) == 2:
    url = "https://jsonplaceholder.typicode.com/todos"
    try:
        int(argv[1])
    except ValueError as e:
        exit
    data = {"userId": argv[1]}
    resp = requests.get(url, params=data).json()
    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    emp_name = requests.get(url).json().get("name")
    with open("{}.csv".format(argv[1]), 'w') as fd:
        fieldnames = ['id', 'name', 'status', 'title']
        writer = csv.DictWriter(fd, fieldnames=fieldnames)
        for task in resp:
            completed = task.get("completed")
            writer.writerow({'id': argv[1], 'name': emp_name,
                             'status': str(completed),
                             'title': task.get("title")})
