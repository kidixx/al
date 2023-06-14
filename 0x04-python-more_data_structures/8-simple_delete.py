#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):

    """
    # Write a function that deletes a key in a dictionary.
    # key argument will be always a string
    # If a key doesn’t exist, the dictionary won’t change
    # VARIABLE(" "):
    # simple_delete(dict): Simple delete by key
    """

    #  in this function, we will check if the given 'key' exists in the...
    #  ...'a_dictionary' using the 'in' operator
    if key in a_dictionary:

        #  If the key exists, we will use the 'del' statement to delete...
        #  ...the key-value pair from the dictionary
        del a_dictionary[key]
    return a_dictionary
