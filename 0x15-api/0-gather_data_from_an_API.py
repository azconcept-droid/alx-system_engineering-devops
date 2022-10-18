#!/usr/bin/python3
"""This module uses REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
import sys


if __name__ == "__main__":
    # Get employee id from command line
    id = sys.argv[1]
    # Assign user and todos endpoints or url to a variable
    users = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    todos = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(id)
    # Sending a get requests to each endpoints
    response_users = requests.get(users)
    response_todos = requests.get(todos)
    # Convert response to a list json format
    user = response_users.json()
    todos_list = response_todos.json()

    name = user.get('name')
    tasks_done = 0
    task_title = []
    # Get total number of tasks
    total_tasks = len(todos_list)
    # Get total number of tasks done and titles list
    for todo in todos_list:
        if todo.get('completed') is True:
            tasks_done += 1
            task_title.append(todo.get('title'))

    print("Employee {} is done with tasks({}/{}):"
          .format(name, tasks_done, total_tasks))
    for title in task_title:
        print("\t {}".format(title))
