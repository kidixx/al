#!/usr/bin/python3


def common_elements(set_1, set_2):

    """
    # Write a function that returns a set of common
    # elements in two sets.
    # VARIABLE(" "):
    # common_elements(set): Present in both
    """

    #  This will find the intersection of
    #  the two sets using the '&' operator
    common_elements_set = set_1 & set_2

    #  This will now return the set of common elements
    return common_elements_set


#  Take for instance
#  set_1 = {"Python", "C", "Javascript"}
#  set_2 = {"Bash", "C", "Ruby", "Pearl"}
#  c_set = common_elements(set_1, set_2)
#  print(c_set)
