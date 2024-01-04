#!/usr/bin/python3
"""Retrieves and exports to-do list information for a specified employee ID to
JSON format."""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(f"{url}users/{user_id}")
    if user_response.status_code == 200:
        user = user_response.json()
        username = user.get("username")
        todos_response = requests.get(f"{url}todos",
                                      params={"userId": user_id})
        if todos_response.status_code == 200:
            todos = todos_response.json()
            todo_list = [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]
            with open(f"{user_id}.json", "w") as jsonfile:
                json.dump({user_id: todo_list}, jsonfile)
        else:
            print(f"Unable to retrieve the TODO list for user ID: {user_id}")
    else:
        print(f"Failed to retrieve user information for ID: {user_id}")
