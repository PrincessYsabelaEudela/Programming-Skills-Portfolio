# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 17:16:47 2023

@author: Cowabonga
"""

"""
Exercise 6: Shrinking Guest List 

You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

•Start with your program from Exercise 4-5. Add a new line that prints a message saying that you can invite only two people for dinner.

•Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.

•Print a message to each of the two people still on your list, letting them know they’re still invited.

•Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.    

"""

dinner = ["Kim Taehyung", "Hoshimachi Suisei", "Taylor Swift"]
for i in dinner: 
    print ("Hello", i + ", I am inviting you for a dinner this Saturday.")
print (dinner[1], "can't make it.")
dinner[1] = ("Selen Tatsuki")
for i in dinner:
    print ("Hello", i + ", I am inviting you for a dinner this Saturday.")
print ("Unfortunately, I can only invite two people for dinner.") #printing message
removed = dinner.pop(1) #pop() removes guest from list
print ("Sorry", removed, "There are no sits available.") #message to the removed guest
for i in dinner: #looping a message for the remainig guests
    print ("Hello", i + ", you are still invited for dinner this Saturday.")
del dinner[:] #deleting the list/emptying the list
print (dinner)
