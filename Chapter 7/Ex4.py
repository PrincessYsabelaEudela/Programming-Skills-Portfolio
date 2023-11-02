# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 11:57:38 2023

@author: Cowabonga
"""

"""
Exercise 4: Large Shirts

Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

"""


def make_shirt(size="large", message="I Love Python"): #function with size and message already assigned(deafault message)
    print('I am going to make a', size, 't-shirt.' ) 
    print('The print would be "' + message + '"')

make_shirt() #defaut message
make_shirt('medium') #the size is changed through calling the value
make_shirt(size="small", message="Metaverse") #the size and message is changed through calling the value