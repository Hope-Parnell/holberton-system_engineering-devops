#!/usr/bin/python3
"""gathers todo info based on input id"""


import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    user_info = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.
        format(user_id)).json()
    name = user_info.get('name')
    tasks_completed = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos?completed=true'.
        format(user_id)).json()
    total_tasks = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.
        format(user_id)).json()

    print('Employee {} is done with tasks({}/{})'.
          format(name, len(tasks_completed), len(total_tasks)))
    for item in tasks_completed:
        print('\t {}'.format(item.get('title')))
