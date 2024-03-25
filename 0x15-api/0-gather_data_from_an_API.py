import requests
import sys

"""Fetches the TODO list for a given employee ID and displays the progress."""


if __name__ == "__main__":
    userId = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(userId))
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    userResponse = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(userId))

    completedTasks = 0
    totalTasks = 0

    for task in todos:
        if task.get('userId') == int(userId):
            totalTasks += 1
            if task.get('completed'):
                completedTasks += 1

    employeeName = userResponse.json()['name']

    print(f"Employee {employeeName} is done with tasks ({completedTasks}/{totalTasks}):")
    print('\n'.join(["\t " + task.get('title') for task in todos
          if task.get('userId') == int(userId) and task.get('completed')]))
