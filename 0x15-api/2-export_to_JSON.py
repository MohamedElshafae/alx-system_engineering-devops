#!/usr/bin/python3
"""Python script to export data in the JSON format"""
import json
from requests import get
from sys import argv


if __name__ == "__main__":

    resource = get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
    tasks = get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}/todos')
    file_path = f'{argv[1]}.json'

    resource = resource.json()
    tasks = tasks.json()
    resource_id = f"{resource['id']}"
    data = {"{}".format(resource_id): []}
    for task in tasks:
        new_data = {
            "task": f"{task['title']}",
            "completed": task['completed'],
            "username": f"{resource['username']}"
        }
        data["{}".format(resource_id)].append(new_data)
    with open(file_path, "w") as file:
        json.dump(data, file)
