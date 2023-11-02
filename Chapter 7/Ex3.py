# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 11:43:44 2023

@author: Cowabonga
"""

"""
Exercise 3: T-Shirt

Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
The function should print a sentence summarizing the size of the shirt and the message printed on it. 
Call the function once using positional arguments to make a shirt. 
Call the function a second time using keyword arguments.

"""

def make_shirt(size, message): #function with size and message
    print('I am going to make a', size, 't-shirt.' ) 
    print('The print would be "' + message + '"')

make_shirt('medium', 'Metaverse')
make_shirt(size="Medium", message="Metaverse")