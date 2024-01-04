#!/usr/bin/python3
"""Fetches information from JSONPlaceholder API and exports to CSV"""

import requests
import csv
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)
    base_url = "https://jsonplaceholder.typicode.com"
    tasks_url = f"{base_url}/user/{sys.argv[1]}/todos"
    user_url = f"{base_url}/users/{sys.argv[1]}"
    tasks_data = requests.get(tasks_url).json()
    user_data = requests.get(user_url).json()
    task_list = []
    for task in tasks_data:
        task_info = {
            "USER_ID": sys.argv[1],
            "USERNAME": user_data.get("username"),
            "TASK_COMPLETED_STATUS": str(task.get("completed")),
            "TASK_TITLE": task.get("title")
        }
        task_list.append(task_info)
    file_name = f"{sys.argv[1]}.csv"
    with open(file_name, 'w', newline='', encoding='utf-8') as csv_file:
        header = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        csv_writer = csv.DictWriter(csv_file, fieldnames=header,
                                    quoting=csv.QUOTE_ALL)
        csv_writer.writeheader()
        csv_writer.writerows(task_list)
