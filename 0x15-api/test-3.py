#!/usr/bin/python3
"""
Check student JSON output
"""

import json
import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"


correct_json = requests.get(users_url).json()

def user_info():
    """ Check user info """
    
    with open('todo_all_employees.json', 'r') as f:
        student_json = json.load(f)

    # print(correct_json)
    # for correct_entry in correct_json:
    #     print(correct_entry['id'])
    # for student_entry in student_json:
    #     print(student_entry)

if __name__ == "__main__":
    user_info()
