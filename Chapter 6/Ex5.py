# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 11:31:28 2023

@author: Cowabonga
"""

"""
Exercise 5: No Pastrami

Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. 
Add code near the beginning of your program to print a message saying the deli has run out of pastrami, 
and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. 
Make sure no pastrami sandwiches end up in finished_sandwiches.

"""

sandwich_orders = ['Pastrami', 'Tuna', 'Egg', 'Pastrami', 'Chicken', 'Pastrami', 'Grilled cheese']
finished_sandwiches = []

print('The deli has ran out of pastrami for today\n')
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')
    
while sandwich_orders: #looping through the list of sandwiches one by one
    current_sandwich = sandwich_orders.pop() #removes the item from the list
    print('I am currently making your', current_sandwich, 'sandwich.') #printing the message
    finished_sandwiches.append(current_sandwich) #the item in in current_sandwich is being added to the finished list

print('\n') #printing a message that each sandwich was made
for sandwich in finished_sandwiches:
    print('I made a', sandwich, 'sandwich')