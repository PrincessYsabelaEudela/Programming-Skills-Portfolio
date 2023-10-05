# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 16:54:11 2023

@author: Cowabonga
"""

"""
Exercise 5: Change Guest List

You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

•Start with your program from Exercise 4. Add a print() call at the end of your program stating the name of the guest who can’t make it.

•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

•Print a second set of invitation messages, one for each person who is still in your list.

"""

dinner = ["Kim Taehyung", "Hoshimachi Suisei", "Taylor Swift"]
for i in dinner: #for loop iterates over the list one by one
    print ("Hello", i + ", I am inviting you for a dinner this Saturday")
print (dinner[1], "can't make it") #calling out the guest who can't come with their position of 1 in the list
dinner[1] = ("Selen Tatsuki") #changing or replacing the person
for i in dinner:
    print ("Hello", i + ", I am inviting you for a dinner this Saturday") #looping agin wiht the new list