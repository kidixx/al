#!/usr/bin/python3

def best_score(a_dictionary):

    """
    # Write a function that returns a key with the
    # ..........biggest integer value.
    # You can assume that all values are only integers
    # VARIABLE(" "):
    # best_score(dict): Best score
    """

    if not a_dictionary:
        return None

    #  in this function, we initialize 'max_key' to 'None' and 'Max_value' to
    #  ...to negative infinity 'float('-inf)
    #  This will handle the case where the dictionary is empty or all values
    #  ...are negative...
    max_key = None
    max_value = float('-inf')

    #  We then iterate over the key-value pairs in the input 'a_dictionary'..
    #  ...using the 'items()' method.
    for key, value in a_dictionary.items():

        #  For each pair, we check if the value is greater than the current..
        #  ..'max_value' ..if it is, we update 'max_key' with the current key
        #  ..and 'max_value' with the current value.
        if value > max_value:
            max_key = key
            max_value = value

    #  After iterating through all the key-value pairs, we return max_key

    return max_key
