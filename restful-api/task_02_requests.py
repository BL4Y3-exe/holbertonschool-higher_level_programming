#!/usr/bin/python3
"""
This module contains fetch_and_print_posts and fetch_and_save_posts
functions.
"""
import requests
import csv

def fetch_and_print_posts():
    """
    Function gets posts from api and prints the titles."""
    res = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {res.status_code}")

    if res.status_code == 200:
        data = res.json()

        for post in data:
            print(post['title'])

def fetch_and_save_posts():
    """
    Function gets posts from api, cleans json file
    and converts ot to csv.
    """
    res = requests.get('https://jsonplaceholder.typicode.com/posts')
    if res.status_code == 200:
        data = res.json()
        clean_data = [
            {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"],
            }
            for post in data
        ]

        with open('posts.csv', 'w', newline='') as f:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(clean_data)
