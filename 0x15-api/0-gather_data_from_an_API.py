#!/usr/bin/python3
"""Using REST API, for a given employee ID, returns information about
his/her TODO list progress."""
import requests
import sys

if __name__ == "__main__":
    ID = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"

    # GET employee data whose userId is passed to the script
    users = requests.get(f"{url}/users/{ID}").json()
    todos = requests.get(f"{url}/todos?userId={ID}").json()

    # Get the number of completed tasks and total number of tasks
    done = sum(1 for task in todos if task.get('completed'))
    total = len(todos)

    # Print employee todo list progress and title of completed tasks
    print(f"Employee {users.get('name')} is done with tasks({done}/{total}):")
    [print(f"\t {task.get('title')}")
     for task in todos if task.get('completed')]
