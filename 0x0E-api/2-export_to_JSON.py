#!/usr/bin/python3
"""gathers todo info based on input id and saves to json"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    user_info = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.
        format(user_id)).json()
    username = user_info.get('username')
    tasks = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.
        format(user_id)).json()

    j_tasks = {user_id: []}

    for task in tasks:
        j_tasks[user_id].append({"task": task.get('title'),
                                 "completed": task.get('completed'),
                                 "username": username})

    with open('{}.json'.format(user_id), 'w') as jsonfile:
        json.dump(j_tasks, jsonfile)
