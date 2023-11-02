# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 11:48:03 2023

@author: Cowabonga
"""

"""
Exercise 3: Print date and Time

Write a Python program to display the current date and time.

"""

import datetime #importing the date and time module from the library
now = datetime.datetime.now() #assigned datetime to the variable now
print ('Current date and time:')
print (now.strftime("%Y-%m-%d %H:%M:%S")) #strftime is used to convert the date and time to different string formats