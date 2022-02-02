# Title: Module_03 Exercise_04
# Author: Wendy Dushanin
# UNCC Student ID: 800727084
# Date: February 1, 2022

# Description: 
# Take in 5 int inputs from the user and add them together. The catch is that you
# can no longer assume that what the user enters is a valid int. If the user enters
# an invalid input, print an error message and make the user input the int again
# until all 5 int values are entered correctly. Print the resulting sum.

# References: 
# https://docs.python.org/3/tutorial/errors.html

# Start Script: 
sum_total = 0 #keeps the count of sum of entered numbers
#Asks users for the elements of list
for i in range(0, 5): #Iterates through a loop of 5 iterations
    while True: #loops until the iterations are complete
        try:
            x = int(input(f'Enter integer #{i+1}: ')) #asks user for integer input
            sum_total += x #adds integer to total sum
            break
        except ValueError: #catches error if anything other than an integer is entered
            print("Invalid input. Please enter an integer.")

print(f'Your sum is: {sum_total}')