#!/usr/bin/python3
"""
Retrieves task-related data for an employee using the JSON Placeholder API
"""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    base_url = 'https://jsonplaceholder.typicode.com'
    employee_id = sys.argv[1]
    tasks_url = f"{base_url}/todos?userId={employee_id}"
    user_url = f"{base_url}/users/{employee_id}"
    try:
        tasks_response = requests.get(tasks_url)
        user_response = requests.get(user_url)
        tasks_data = tasks_response.json()
        user_data = user_response.json()
        if (tasks_response.status_code != 200 or
           user_response.status_code != 200):
            print("Failed to fetch data. Please check the employee ID.")
            sys.exit(1)
        total_tasks = len(tasks_data)
        completed_tasks = sum(1 for task in tasks_data if task['completed'])
        employee_name = user_data.get("name")
        print(f"Employee {employee_name} is done with tasks "
              f"({completed_tasks}/{total_tasks}): ")
        for task in tasks_data:
            if task['completed']:
                print(f"\t{task['title']}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        sys.exit(1)
