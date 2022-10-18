#!/usr/bin/python3
"""This module uses REST API, for a given employee ID,
returns information about his/her TODO list progress
in CSV format
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
    # Convert response to a json format
    user = response_users.json()
    todos_list = response_todos.json()

    name = user.get('username')
    filename = "{}.json".format(user.get('id'))

    # save data in csv format
    with open(filename, mode='w') as file:
        for todo in todos_list:
            dict_list = []
            task_done = todo.get('completed')
            task_title = todo.get('title')
            #"\"task\": \"{}\", \"completed\": {}, \"username\": \"{}\"".format(task_title, task_done, name)
            dict_list.append(task_title)
            #{"{}": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ...]}
            file.write("{}".format(dict_list))
