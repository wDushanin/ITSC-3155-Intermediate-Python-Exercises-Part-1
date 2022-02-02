# Title: Module_03 Exercise_01
# Author: Wendy Dushanin
# UNCC Student ID: 800727084
# Date: February 1, 2022

# Description:
# Write a function that takes in a list data structure as input. The function should
# create a new list and only include unique elements of the inputted list. Under the
# function, write code that calls the function with a test list like so and print out the result

# References: 
# https://www.w3resource.com/python-exercises/python-functions-exercise-8.php


#Start of Function: 

def get_unique_list(x):#function that takes a list argument
    list = []#empty list to store uniqe values
    for num in x: #iterates through list input to function
        if num not in list: #when elemet not in the empty list is found
            list.append(num)#add that element to the empty list
    return list #return unique list after iteration is completed

#Test Code
my_list = [1, 2, 3, 2, 1, 4]
unique_list = get_unique_list(my_list)
print(unique_list)
