#!/usr/bin/python3
"""This module contains convert_csv_to_json function."""
import csv
import json


def convert_csv_to_json(filename):
    """
    Function converts csv to json.

    Args:
        filename: name of the file.
    """
    try:
        data = []

        with open(filename, 'r', encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                data.append(row)

        with open("data.json", 'w', encoding="utf=8") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except Exception:
        return False
