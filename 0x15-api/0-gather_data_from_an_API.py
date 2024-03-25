#!/usr/bin/python3
"""Fetches the TODO list for a given employee ID and displays the progress."""

import requests
import sys


if __name__ == "__main__":
    userId = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                        .format(userId))
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()
    userResponse = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(userId))
    employeeName = userResponse.json().get('name')

    completedTasks = 0
    totalTasks = 0

    for task in todos:
        if task.get('userId') == int(userId):
            totalTasks += 1
            if task.get('completed'):
                completedTasks += 1


    print("Employee {} is done with tasks ({}/{}):"
          .format(employeeName, completedTasks, totalTasks))
    print('\n'.join(["\t " + task.get('title') for task in todos
          if task.get('userId') == int(userId) and task.get('completed')]))
