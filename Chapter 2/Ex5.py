# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 14:10:36 2023

@author: Cowabonga
"""

"""
Exercise 5: USB Shopper

A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.

Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.

You will to use the arithmetic operators to complete this exercise.

"""
import math #importing math from library to use the floor function
money = 50
cost = 6
amount = money/cost #amount of USB she can buy
rounddown = math.floor(amount) #the floor function rounds down the float as you can't have 0.5 or 0.something of a stick
Total = rounddown*cost #calculating the total cost
change = money-Total 
print ("She can buy", rounddown, "USB sticks")
print ("She will have £" + str(change) + " left") 
#I changed the change variable to a string because I don't want a space between the pound sign and change, I want the change next to the sign. 
#To do that I used plus instead of comma and it won't work if its's not a string