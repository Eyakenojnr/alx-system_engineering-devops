#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    ID = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    # GET employee data whose userId is passed to the script
    users = requests.get(f"{url}/users/{ID}").json()
    todos = requests.get(f"{url}/todos?userId={ID}").json()

    # Create csv file and write data to it
    csv_file = f"{ID}.csv"
    with open(csv_file, mode='w', newline='') as file:
        # quoting=csv.QUOTE_ALL ensures output is quoted
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [ID, users.get('username'), task.get('completed'),
             task.get('title')]) for task in todos]
