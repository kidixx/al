#!/usr/bin/python3


def uniq_add(my_list=[]):

    """
    # Write a function that adds all unique integers in
    # a list (only once for each integer).
    # VARIABLE(" "):
    # uniq_add(list): Unique addition
    """

    #  This line creates a set to store unique integers
    uniq_numb = set()

    #  This line will iterate over the element in the list
    for numb in my_list:

        #  Adding each integer to the set
        #  (duplicates will be automatically ignored)
        uniq_numb.add(numb)

    #  calculates the sum of the unique integers
    sum_uniq_numb = sum(uniq_numb)

    #  This will return the sum
    return sum_uniq_numb


#  Take for instance
#  my_list = [1, 2, 3, 1, 4, 2, 5]
#  Result = uniq_add(my_list)
#  print("Result: {}".format(Result))
#  print(my_list)
