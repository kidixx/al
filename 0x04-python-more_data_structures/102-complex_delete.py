#!/usr/bin/python3

def complex_delete(a_dictionary, value):

    """
    # Write a function that deletes keys with a specific value in a dictionary
    # ...If the value doesn’t exist, the dictionary won’t change
    # All keys having the searched value have to be deleted
    # VARIABLE(" "):
    # complex_delete(dict): Delete by value
    """

    delete_key = [key for key, val in a_dictionary.items() if val == value]
    for key in delete_key:
        del a_dictionary[key]
    return a_dictionary
