#!/usr/bin/python3

def weight_average(my_list=[]):

    """
    # Write a function that returns the weighted average
    # of all integers tuple (<score>, <weight>)
    # VARIABLE(" "):
    # weight_average(list): Weighted average!
    # Returns: 0 if the list is empty
    """

    if not my_list:
        return 0

    total_sum = 0
    total_weight = 0

    for score, weight in my_list:
        total_sum += score * weight
        total_weight += weight

    return total_sum / total_weight
