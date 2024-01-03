#!/usr/bin/python3
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


def fetch_employee_todo_progress(employee_id):
    base_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    t_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    try:
        user_response = requests.get(base_url)
        user_data = user_response.json()
        employee_name = user_data['name']
        todos_response = requests.get(t_url)
        todos_data = todos_response.json()
        total_tasks = len(todos_data)
        completed_tasks = sum(1 for todo in todos_data if todo['completed'])
        print(f"Employee {employee_name} is done with tasks "
              f"({completed_tasks}/{total_tasks}): ")
        for todo in todos_data:
            if todo['completed']:
                print(f"\t{todo['title']}")
    except requests.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    fetch_employee_todo_progress(employee_id)
