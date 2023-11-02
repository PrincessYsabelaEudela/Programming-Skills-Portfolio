# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 23:15:14 2023

@author: Cowabonga
"""

"""
Exercise 1: Pizza Toppings

Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. 
As they enter each topping, print a message saying you’ll add that topping to their pizza.

"""

while True:
    topping = (input("What toppings would you like? \nEnter 'quit' if you want to stop adding toppings:") ) #user input for toppings and quit
    if topping != 'quit': #if user input is not quit print message else break or stop the loop
        print("Adding", topping, "to pizza")
    else:
        break;
