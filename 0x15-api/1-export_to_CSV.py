#!/usr/bin/python3
"""This Script exports data in CSV format"""
import csv
import requests as r
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    usr_response = r.get(f"{url}users/{user_id}")
    if usr_response.status_code == 200:
        usr = usr_response.json()
        username = usr.get("username")
        todo_response = r.get(f"{url}todos", params={"userId": user_id})
        if todo_response.status_code == 200:
            to_do = todo_response.json()
            with open(f"{user_id}.csv", "w", newline="") as csvfile:
                writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
                for elm in to_do:
                    writer.writerow([user_id, username, elm.get("completed"),
                                     elm.get("title")])
        else:
            print(f"Failed to retrieve TODO list for user ID: {user_id}")
    else:
        print(f"Failed to retrieve user information for ID: {user_id}")
