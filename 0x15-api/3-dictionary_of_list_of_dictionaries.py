#!/usr/bin/python3
"""Python script to export data in the JSON format"""
import json
from requests import get
from sys import argv


if __name__ == "__main__":

    users = get(f'https://jsonplaceholder.typicode.com/users')
    file_path = f'todo_all_employees.json'

    users = users.json()
    data = {}
    for user in users:
        tasks = get(f'https://jsonplaceholder.typicode.com/users/'
                    f'{user["id"]}/todos').json()
        for task in tasks:
            new_data = {
                "task": f"{task['title']}",
                "completed": task['completed'],
                "username": f"{user['username']}"
            }
        data["{}".format(user['id'])] = new_data
    with open(file_path, "w") as file:
        json.dump(data, file)
