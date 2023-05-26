#!/usr/bin/python3
"""Script to export data in the CSV format"""

if __name__ == "__main__":

    import csv
    import requests
    import sys as s

    userId = s.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))
    name = user.json().get('username')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    filename = userId + '.csv'
    with open(filename, mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in todos.json():
            if task.get('userId') == int(userId):
                writer.writerow([userId, name, str(task.get('completed')),
                                 task.get('title')])
