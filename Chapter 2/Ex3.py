# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 13:40:45 2023

@author: Cowabonga
"""

"""
Exercise 3: Stripping Names

Tidy up the code to make it easier to understand

Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, “\t” and “\n”, at least once.

Print the name once, so the whitespace around the name is displayed.

Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

"""

a = (" \tPrincess Ysabela Eudela\t")
print (a) #printing a
print (a.strip()) #strip() removes start and end spaces
print (a.rstrip()) #rstrip() removes end spaces
print (a.lstrip()) #lstrip() removes start spaces