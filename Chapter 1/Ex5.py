# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 10:24:31 2023

@author: Cowabonga
"""

"""
Exercise 5: Compute area of Circle

Write a Python program which accepts the radius of a circle from the user and compute the area.

"""

from math import pi #specifically importing pii from the math library
r = float(input("Enter the radius:")) #user input for radius
a = pi * r**2 #variable a is the calculation of area
ro = round(a, 2) #variable ro is the rounds the area using the round function 
print ("Area =", ro)