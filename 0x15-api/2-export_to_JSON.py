#!/usr/bin/env python3
"""
This script retrieves and displays information about an employee's
TODO list progress
from a REST API based on the provided employee ID.

Requirements:
- Utilizes the requests module
- Accepts an integer as a parameter (employee ID)
- Displays the employee's TODO list progress in a specific format
"""

import requests
import sys
import json


def fetch_employee_todo_progress(employee_id):
    base_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    t_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    try:
        user_response = requests.get(base_url)
        user_data = user_response.json()
        employee_name = user_data['name']
        todos_response = requests.get(t_url)
        todos_data = todos_response.json()
        json_filename = f"{employee_id}.json"
        employee_tasks = []
        for todo in todos_data:
            task_details = {
                "task": todo['title'],
                "completed": todo['completed'],
                "username": employee_name
            }
            employee_tasks.append(task_details)
        with open(json_filename, 'w') as jsonfile:
            json.dump({f"USER_ID": employee_tasks}, jsonfile, indent=2)
        print(f"Data exported to {json_filename} successfully!")
    except requests.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    fetch_employee_todo_progress(employee_id)
