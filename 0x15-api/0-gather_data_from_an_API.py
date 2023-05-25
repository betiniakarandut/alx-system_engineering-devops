#!/usr/bin/python3
"""Script that gathers user information from an API
and display their TODO list progress"""

import requests
import sys as s

if __name__ == "__main":

    employee_id = s.argv[1]
    userId = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(employee_id))

    name = user.json().get('name')

    todos = requests.get("https://jsonplaceholder.typicode.com/users/todos")
    totalTask = 0
    completed = 0

    for tasks in todos.json():
        if task.get('userId') == int(userId):
            totaltask += 1
            if task.get('completed'):
                completed +=1

    print("Employee {} is done with tasks({}/{}):".format(name, completed, totalTask))

    print('\n'.join(["\t " + task.get('title') for task in todos.json()
          if task.get('userId') == int(userId) and task.get('completed')]))


