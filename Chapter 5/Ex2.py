# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 21:30:03 2023

@author: Cowabonga
"""

"""
Exercise 2: Glossary

Think of five programming words you’ve learned about in the previous chapters. 
Use these words as the keys in your glossary, and store their meanings as values.
Print each word and its meaning as neatly formatted output. 
You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. 
Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

"""
#dictionary glossary that stores the key(word) and values(meaning)
glossary = {'String': 'It is a data type, these are words or alphabet characters',
            'Float': 'It is a data type that are numbers that have a decimal point',
            'Bitwise Operator': 'They operate bit by bit, the values are converted to binary, does the computation, then convert it back into a decimal',
            'Slicing': 'extracts data that is part of a list, string or tuple',
            'List': 'It stores multiple data or items in a single variable'}

for key, value in glossary.items(): #iterates or loops the key and value pair in the dictionary and prints them
    print(key,':', value, '\n') 