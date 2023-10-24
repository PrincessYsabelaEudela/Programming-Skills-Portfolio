# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 12:30:01 2023

@author: Cowabonga
"""

"""
Exercise 4: Stages of Life

•If the person is less than 2 years old, print a message that the person is a baby.

•If the person is at least 2 years old but less than 4, print a message that the person is a toddler.

•If the person is at least 4 years old but less than 13, print a message that the person is a kid.

•If the person is at least 13 years old but less than 20, print a message that the person is a teenager.

•If the person is at least 20 years old but less than 65, print a message that the person is an adult.

•If the person is age 65 or older, print a message that the person is an elder.

"""

age = int(input("Age:"))
if age < 2: #less than 2 years old
    print("You are a baby")
elif age>= 2 and age<4: #2 years old but less than 4
    print("You're a toddler")
elif age>= 4 and age<13: #4 years old but less than 13
    print("You're a kid")
elif age>= 13 and age<20: #13 years old but less than 20
    print("You're a teenager") 
elif age>= 20 and age<65: #20 years old but less than 65
    print("You're an adult") 
else: #65 or older
    print("You're an elder")