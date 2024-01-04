#!/usr/bin/python3
"""Exports task information for all employees to a JSON file."""
import json
import requests as req


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    employee_data = req.get(base_url + "users").json()
    with open("todo_all_employees.json", "w") as json_file:
        json.dump({
            emp.get("id"): [
                {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": emp.get("username")
                }
                for task in req.get(base_url + "todos",
                                    params={"userId": emp.get("id")}).json()
            ]
            for emp in employee_data
        }, json_file)
