#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    """
    # Write a function that returns a new dictionary
    # with all values multiplied by 2
    # You can assume that all values are only integers
    # Return: a new dictionary
    # VARIABLE(" "):
    # multiply_by_2(dict): Multiply by 2
    """

    #  in this function, we create am empty dictionary called 'new_dict' to
    #  store the updated values.
    new_dict = {}

    #  We can then iterate over the key-value  pairs in the input..
    #  ...'a_dictionary' using 'items()' method.
    for key, value in a_dictionary.items():

        #  for each pair, we multiply the value by 2 and assign the result
        #  key in 'new_dict' 
        new_dict[key] = value * 2

        #  finally, we return the 'new_dict' with all values multiplied by 2 
    return new_dict
