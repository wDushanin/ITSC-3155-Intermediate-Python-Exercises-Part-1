# Title: Module_03 Exercise_02
# Author: Wendy Dushanin
# UNCC Student ID: 800727084
# Date: February 1, 2022

# Description:
#  Write a function that takes in two dict data structures as input. Both dicts map
# str->int (the keys are strings and the values are integers). The function should
# compute a new dict which combines the two dicts by summing the values for the
# common keys. Keys that are not common should be left out.

# References: 
# https://www.geeksforgeeks.org/python-combine-two-dictionary-adding-values-for-common-keys/


# Start of Function: 

def get_combined_dict(x, y): #function that takes two dict arguments
    new_dict = {} #empty dictonary to store the result of function
    for key, value in x.items():#iterates through x dict 
        if (key in y.keys()):#if key is found in y dict, add the value from x
            new_dict[key] = value + y[key]#adds new value and key to the "empty" dict
    return new_dict

# Test Code: 

my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)
