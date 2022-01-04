#!/usr/bin/python3
"""gathers todo info based on input id and saves to csv"""


import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    user_info = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.
        format(user_id)).json()
    username = user_info.get('username')
    tasks = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.
        format(user_id)).json()

    with open('{}.csv'.format(user_id), 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([user_id, username, task.get('completed'),
                            task.get('title')])
