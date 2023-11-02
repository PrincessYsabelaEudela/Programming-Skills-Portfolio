# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 12:25:03 2023

@author: Cowabonga
"""

"""
Exercise 3: Alien Colors #3

Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.

• If the alien is green, print a message that the player earned 5 points.

• If the alien is yellow, print a message that the player earned 10 points.

• If the alien is red, print a message that the player earned 15 points.

• Write three versions of this program, making sure each message is printed for the appropriate color alien.

"""

"""
green

"""

alien_color = ("green") #variable assigned with the value of green
if alien_color == "green":
    print ("You earned 5 points") #prints the message
elif alien_color == "yellow":
    print ("You earned 10 points")
else:
    print ("You earned 15 points")
    
"""
yellow

"""

alien_color = ("yellow") #variable assigned with the value of yellow
if alien_color == "green":
    print ("You earned 5 points")
elif alien_color == "yellow":
    print ("You earned 10 points") #prints the message
else:
    print ("You earned 15 points")
    
"""
red

"""

alien_color = ("red") #variable assigned with the value of red
if alien_color == "green":
    print ("You earned 5 points")
elif alien_color == "yellow":
    print ("You earned 10 points")
else:
    print ("You earned 15 points") #prints the message