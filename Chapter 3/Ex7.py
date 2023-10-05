# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 17:35:42 2023

@author: Cowabonga
"""

"""
Exercise 7: Seeing the World

1. Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.

2. Use sorted() to print your list in alphabetical order without modifying the actual list.

3. Show that your list is still in its original order by printing it.

4. Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.

5. Show that your list is still in its original order by printing it again.

6. Use reverse() to change the order of your list. Print the list to show that its order has changed.

7. Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.

8. Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.

9 Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
"""

loc = ["Japan", "S. Korea", "Finland", "Canada", "Georgia"]
print ("Original:", loc) #Q1 printing list
print ("Alphabetical Sorted:", sorted(loc)) #Q2
print ("Original:", loc) #Q3
print ("Descending Sorted:", sorted(loc, reverse= True)) #Q4
print ("Original:", loc) #Q5
reverse = (list(reversed(loc))) #Q6 | reverse only the order not by alphabet
print ("Reverse:", reverse) #Q6
print ("Reverse Reverse:", (list(reversed(reverse)))) #Q7 | original order
loc.sort()
print ("Alphabetical Sort:", loc) #Q8
loc.sort(reverse=True)
print ("Descending Sort:", loc) #Q9
