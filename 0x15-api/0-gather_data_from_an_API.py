#!/usr/bin/python3
"""
Script to retrieve information about an employee's TODO list progress
using a REST API.
"""
import requests
import sys


def get_user_info(user_id):
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_response = requests.get(f'{base_url}users/{user_id}')
    if user_response.status_code == 200:
        return user_response.json()
    else:
        print(f"Failed to retrieve user information for ID: {user_id}")
        return None


def get_user_todo_list(user_id):
    base_url = 'https://jsonplaceholder.typicode.com/'
    todo_response = requests.get(f'{base_url}todos',
                                 params={'userId': user_id})
    if todo_response.status_code == 200:
        return todo_response.json()
    else:
        print(f"Failed to retrieve TODO list for user ID: {user_id}")
        return None


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
        sys.exit(1)
    employee_id = sys.argv[1]
    user_info = get_user_info(employee_id)
    if user_info:
        user_name = user_info.get("name")
        todo_list = get_user_todo_list(employee_id)
        if todo_list:
            completed_tasks = [title.get("title") for title in todo_list
                               if title.get('completed')]
            num_completed = len(completed_tasks)
            num_total_tasks = len(todo_list)
            print(f"Employee {user_name} has completed "
                  f"{num_completed}/{num_total_tasks} tasks: ")
            for task in completed_tasks:
                print(f"\t{task}")
        else:
            print("No TODO list found for the specified employee ID.")
    else:
        print("Employee information not found for the specified ID.")
