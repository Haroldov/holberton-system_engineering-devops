#!/usr/bin/python3
""" doc """

import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos"
    data = {"userId": argv[1]}
    resp = requests.get(url, params=data).json()
    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    emp_name = requests.get(url).json().get("name")
    completed_tasks = []
    for task in resp:
        if task.get("completed") is True:
            completed_tasks.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
        emp_name, len(completed_tasks), len(resp)))
    for title in completed_tasks:
        print("\t{}".format(title))
