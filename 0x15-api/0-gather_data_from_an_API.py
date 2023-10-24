#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""

from sys import argv
from requests import get


if __name__ == "__main__":
    resource = get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
    tasks = get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}/todos')

    done_task = []

    resource = resource.json()
    tasks = tasks.json()
    len_tasks = len(tasks)

    for task in tasks:
        if task.get('completed') is True:
            done_task.append(task.get('title'))
    print(f'Employee {resource.get("name")} is done with tasks({len(done_task)}/{len_tasks}):')
    for task_title in done_task:
        print(f'\t{task_title}')
