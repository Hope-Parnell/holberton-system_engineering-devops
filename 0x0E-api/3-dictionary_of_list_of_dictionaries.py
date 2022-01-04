#!/usr/bin/python3
"""saves todo info for all users in json"""
import json
import requests


if __name__ == "__main__":
    j_tasks = {}
    users = requests.get('https://jsonplaceholder.typicode.com/users/').json()
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        user_info = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.
            format(user_id)).json()
        username = user_info.get('username')
        tasks = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}/todos'.
            format(user_id)).json()

        j_tasks[user_id] = []

        for task in tasks:
            j_tasks[user_id].append({"username": username,
                                     "task": task.get('title'),
                                     "completed": task.get('completed')})

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(j_tasks, jsonfile)
