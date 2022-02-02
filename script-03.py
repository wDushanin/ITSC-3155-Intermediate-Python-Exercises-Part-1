# Title: Module_03 Exercise_03
# Author: Wendy Dushanin
# UNCC Student ID: 800727084
# Date: February 1, 2022

# Description: Take in a string from the user and pass it as input to a function. Have the
# function return a dict which keeps count of each letter (in lowercase) in the
# string, excluding spaces. Print out this dict.


# References: 
# https://www.geeksforgeeks.org/python-frequency-of-each-character-in-string/

# Function: 

def get_frequency(string):
    #Empty dictionary to store count
    frequency = {}

    #Remove whitespaces from input string
    string = string.replace(' ', '')#finds first argument and replaces with second argument

    #Convert all letters in string to lowercase letters
    string = string.lower() #built in string function

    for letter in string: #iterates through the letters (characters) in the string
        if letter in frequency: #if the letter is already present
            frequency[letter] += 1 #increase count by one
        else: 
            frequency[letter] = 1 #if not present, set count to one
    return frequency 

# Test Code: 
string_test = input('Enter a string: ')

print(get_frequency(string_test))