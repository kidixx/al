#!/usr/bin/python3
"""
Function that converts a JSON string to a python object (data structure)
"""
import json


def from_json_string(my_str):
    """
    # Write a function that returns an object (Python data structure)
    # ....represented by a JSON string:
    # Prototype: def from_json_string(my_str):
    # VARIABLE(" "):
    # from JSON(str): From JSON string to Object
    # Return: Always 0. (Success)
    """
    """
    The 'from_json_string' function is defined with a single parameter...
    'my_str', which represents the JSON string to be converted to a python obj
    """
    """
    The 'loads()' function is used to parse the JSON string as input
    """
    return json.loads(my_str)
    """
    Then, we would return the Python Object representation of the JSON string
    """
