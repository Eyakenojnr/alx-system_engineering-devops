#!/usr/bin/python3
"""Exports to-do list information of all employees in JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get(f"{url}/users/").json()
    todos = requests.get(f'{url}/todos/').json()

    # Prepare JSON data to export
    all_tasks = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        tasks_for_user = [{'username': username, 'task': task.get('title'),
                           'completed': task.get('completed')}
                          for task in todos if task.get('userId') == user_id]
        # Correctly add tasks for each user to all_tasks dictionary
        all_tasks[user_id] = tasks_for_user

    # Export data to JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_tasks, jsonfile)
