# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 21:55:28 2023

@author: Cowabonga
"""

"""
Exercise 3: Glossary 2

Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()
calls with a loop that runs through the dictionary’s keys and values. 
When you’re sure that your loop works, add five more Python terms to your glossary.
When you run your program again, these new words and meanings should automatically be included in the output.

"""
#dictionary glossary that stores the key(word) and values(meaning)
glossary = {'String': 'It is a data type, these are words or alphabet characters',
            'Float': 'It is a data type that are numbers that have a decimal point',
            'Bitwise Operator': 'They operate bit by bit, the values are converted to binary, does the computation, then convert it back into a decimal',
            'Slicing': 'extracts data that is part of a list, string or tuple',
            'List': 'It stores multiple data or items in a single variable'}

for key, value in glossary.items(): #iterates or loops the key and value pair in the dictionary and prints them
    print(key,':', value, '\n') 
    
#adding more key and value to the dictionary
glossary['Dictionary'] = 'A data structure used to store values in a pair of key:value' #adds a new pair or key:value
glossary['Function'] = 'A reusable block of code that only works when it is called'
glossary['Variable'] = 'A container to store data values'
glossary['Loop'] = 'It repeats or go back to the code, one at a time'
glossary['Comment'] = 'A note in the program that is ignored by the interpreter'

print("Updated glossary:") #printing the updated dictionary
for key, value in glossary.items(): 
    print(key,':', value, '\n')