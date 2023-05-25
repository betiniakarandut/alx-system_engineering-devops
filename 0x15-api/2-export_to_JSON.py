#!/usr/bin/python3
"""Script to export data in the JSON format."""

if __name__ == "__main__":

    import json
    import requests
    import sys as s

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()

    todoUser = {}
    taskList = []

    for task in todos:
        if task.get('userId') == int(userId):
            taskDict = {"task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": user.json().get('username')}
            taskList.append(taskDict)
    todoUser[userId] = taskList

    filename = userId + '.json'
    with open(filename, mode='w') as f:
        json.dump(todoUser, f)
