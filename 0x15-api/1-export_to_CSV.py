#!/usr/bin/python3
"""Python script to export data in the CSV format"""

from requests import get
from sys import argv


if __name__ == "__main__":

    resource = get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
    tasks = get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}/todos')
    file_path = 'USER_ID.csv'

    resource = resource.json()
    tasks = tasks.json()
    formated_str = ''
    for task in tasks:
        formated_str += f'"{resource["id"]}","{resource["name"]}",'
        formated_str += f'"{task["completed"]}","{task["title"]}"\n'
    with open(file_path, "w") as file:
        file.write(formated_str)
