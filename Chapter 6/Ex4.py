# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 10:03:30 2023

@author: Cowabonga
"""

"""
Exercise 4: Deli

Make a list called sandwich_orders and fill it with the names of various sandwiches. 
Then make an empty list called finished_sandwiches.
Loop through the list of sandwich orders and print a message for each order, 
such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. 
After all the sandwiches have been made, print a message listing each sandwich that was made.

"""

sandwich_orders = ['Tuna', 'Egg', 'Chicken', 'Grilled cheese']
finished_sandwiches = []

while sandwich_orders: #looping through the list of sandwiches one by one
    current_sandwich = sandwich_orders.pop() #removes the item from the list
    print('I am currently making your', current_sandwich, 'sandwich.') #printing the message
    finished_sandwiches.append(current_sandwich) #the item in in current_sandwich is being added to the finished list

print('\n') #printing a message that each sandwich was made
for sandwich in finished_sandwiches:
    print('I made a', sandwich, 'sandwich')
