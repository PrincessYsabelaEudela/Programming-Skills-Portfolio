# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 22:32:47 2023

@author: Cowabonga
"""

"""
Exercise 5: Pets

Make several dictionaries, where each dictionary represents a different pet. 
In each dictionary, include the kind of animal and the owner’s name. 
Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet

"""
pets = [] #making a list to store the dictionary

#pet dictionary
pet = {'Owner':'Princess',
        'Breed':'Himalayan Cat',
        'Name': 'Karupin'}

pets.append(pet) #inserting the pet dictionary to the list

#pet dictionary
pet = {'Owner':'Ysabela',
        'Breed':'Golden Retriever',
        'Name': 'Winter'}

pets.append(pet) #inserting the pet dictionary to the list

#pet dictionary
pet = {'Owner':'Ela',
        'Breed':'Pomeranian',
        'Name': 'Yeontan'}

pets.append(pet) #inserting the pet dictionary to the list

for pet in pets: #loop the llist to print the info one by one
    print("\nHere's some info about",  pet['Name'].title()+':')
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))

