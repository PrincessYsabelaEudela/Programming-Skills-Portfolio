# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 23:49:29 2023

@author: Cowabonga
"""

"""
Exercise 2: Movie Tickets

A movie theater charges different ticket prices depending on a person’s age. 
If a person is under the age of 3, the ticket is free; 
if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. 
Write a loop in which you ask users their age, and then tell them the cost of their movie ticket

"""

age=int(input("Age:"))
if age<=2: #age is 2 or less
    print('Free ticket')
elif age>=3 and age<=12: #age is 3-12
    print('The tickets are $10')
else: #age is more than 13 and above
    print('The tickets are $15')
    