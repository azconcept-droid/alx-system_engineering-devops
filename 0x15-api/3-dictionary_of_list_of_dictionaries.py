#!/usr/bin/python3
"""This module uses REST API, for a given user ID,
records all tasks from all employees in JSON format
"""

import json
import requests


if __name__ == "__main__":
    # todos endpoints
    todos = 'https://jsonplaceholder.typicode.com/todos?userId=1'
    # Sending a get requests to endpoints
    response_todos = requests.get(todos)
    # Convert response to a json format
    todos_list = response_todos.json()

    filename = "todo_all_employees.json"
    # Prepare data
    # { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
    # "completed": TASK_COMPLETED_STATUS},
    # {"username": "USERNAME", "task": "TASK_TITLE",
    # "completed": TASK_COMPLETED_STATUS}, ... ],
    # "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
    # "completed": TASK_COMPLETED_STATUS},
    # {"username": "USERNAME", "task": "TASK_TITLE",
    # "completed": TASK_COMPLETED_STATUS}, ... ]}
    data = []
    for id in range(1, 11):
        users = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
        response_users = requests.get(users)
        user = response_users.json()
        name = user.get('username')
        for todo in todos_list:
            task_done = todo.get('completed')
            task_title = todo.get('title')

            data.append({
                "username": name,
                "task": task_title,
                "completed": task_done,
            })

    # Write the JSON data to a file
    with open(filename, mode='w') as file:
        json.dump({1: data}, file)
