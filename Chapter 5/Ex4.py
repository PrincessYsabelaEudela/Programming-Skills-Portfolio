# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 22:14:56 2023

@author: Cowabonga
"""

"""
Exercise 4: Rivers

Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

Use a loop to print the name of each river included in the dictionary.

Use a loop to print the name of each country included in the dictionary.

"""

river = {'Nile':'Egypt',
         'Mackenzie': 'Canada',
         'Missouri':'United States',
         'Yangtze':'China',
         'Ob':'Russia'}

for key, value in river.items(): #iterates or loops the key and value pairs in the dictionary and prints them in a sentence
    print('The', key, 'river runs through', value + '.')
    
print("\nThe rivers in the dictionary are:") #prints the key or river in a dash list
for k in river.keys():
    print('-',k)
    
print("\nThe countries in the dictionary are:") #prints the value or countries in a dash list
for v in river.values():
    print('-',v)