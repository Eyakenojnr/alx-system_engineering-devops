#!/usr/bin/python3
"""Exports to-do list information for a given employee ID in JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    ID = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    # GET employee data whose userID is passed to the script
    users = requests.get(f"{url}/users/{ID}").json()
    todos = requests.get(f"{url}/todos?userId={ID}").json()

    # Prepare json data to export
    export_data = {"USER_ID": []}
    for task in todos:
        task_data = {
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': users.get('username')
        }
        export_data["USER_ID"].append(task_data)

    # Export data to JSON file
    json_file = f"{ID}.json"
    with open(json_file, "w") as file:
        json.dump(export_data, file)
