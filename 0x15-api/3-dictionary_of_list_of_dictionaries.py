#!/usr/bin/python3
"""
This script retrieves and exports information about all employees' TODO lists
progress from a REST API in JSON format.

Requirements:
- Utilizes the requests module
- Exports all employees' TODO list progress in JSON format

Usage:
python script.py
"""

import requests
import json
import sys


def fetch_all_employees_todo_progress():
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    try:
        users_response = requests.get(users_url)
        users_data = users_response.json()
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()
        all_employees_tasks = {}
        for user in users_data:
            user_id = user['id']
            employee_name = user['username']
            employee_tasks = []
            for todo in todos_data:
                if todo['userId'] == user_id:
                    task_details = {
                        "username": employee_name,
                        "task": todo['title'],
                        "completed": todo['completed']
                    }
                    employee_tasks.append(task_details)
            all_employees_tasks[user_id] = employee_tasks
        json_filename = "todo_all_employees.json"
        with open(json_filename, 'w') as jsonfile:
            json.dump(all_employees_tasks, jsonfile, indent=2)
        print(f"Data exported to {json_filename} successfully!")
    except requests.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    fetch_all_employees_todo_progress()
