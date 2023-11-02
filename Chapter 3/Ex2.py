# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 15:02:26 2023

@author: Cowabonga
"""

"""
Exercise 2: Greetings

Start with the list you used in Exercise 1, but instead of just printing each person’s name, print a message to them. 
The text of each message should be the same, but each message should be personalized with the person’s name.

"""

names = ["Mariel", "Erin", "Yumnah", "Shiza"]
for N in names: #using for loop to print a message with their personalized name
    print ("Hello", N + ", how are you?" ) #for loop iterates over the list one by one