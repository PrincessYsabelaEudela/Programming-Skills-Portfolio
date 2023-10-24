# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 12:02:54 2023

@author: Cowabonga
"""

"""
Exercise 5: Cities

Write a function called describe_city() that accepts the name of a city and its country. 
The function should print a simple sentence, such as Reykjavik is in Iceland. 
Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the default country.

"""

def describe_city(city, country = 'Philippines'): #function with default country
    print(city, 'is a city in', country + ".")
    
describe_city('Boracay') #calling the value of the city
describe_city('Dubai', 'UAE') #the city and country is changed through calling the value
describe_city('Manila') #calling the value of the city