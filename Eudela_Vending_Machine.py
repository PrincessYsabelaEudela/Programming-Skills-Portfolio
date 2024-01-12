# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 22:48:27 2023

@author: Cowabonga
"""

# Vending Machine Menu
item_classic = [
    {"item_code": "A01", "item_name": "Black Forest", "item_price": 15.00},
    {"item_code": "A02", "item_name": "Classic Chocolate Cake", "item_price": 12.00},
    {"item_code": "A03", "item_name": "Strawberry Cake", "item_price": 12.00},
    {"item_code": "A04", "item_name": "Cheesecake", "item_price": 15.00},
    {"item_code": "A05", "item_name": "Red Velvet Cake", "item_price": 16.50}
]

item_special = [
    {"item_code": "B01", "item_name": "Tiramisu Cake", "item_price": 18.75},
    {"item_code": "B02", "item_name": "Strawberry Shortcake", "item_price": 16.50},
    {"item_code": "B03", "item_name": "Oreo Cookies and Cream Cake", "item_price": 16.00},
    {"item_code": "B04", "item_name": "Matcha Cake", "item_price": 15.50},
    {"item_code": "B05", "item_name": "Mango Passionfruit Cheesecake", "item_price": 14.50}
]

item_drinks = [
    {"item_code": "C01", "item_name": "Cappuccino", "item_price": 5.50},
    {"item_code": "C02", "item_name": "Latte", "item_price": 7.00},
    {"item_code": "C03", "item_name": "Chai", "item_price": 3.00},
    {"item_code": "C04", "item_name": "Hot Chocolate", "item_price": 5.50},
    {"item_code": "C05", "item_name": "Water", "item_price": 1.50}
]

items = {"Classic": item_classic, "Special": item_special, "Drinks": item_drinks}
cart = []
money = 0


def display_menu(category, item_list): #This displays the menu for that category. 
    print(f"\n{category} Menu:")
    for item in item_list: #The loop iterates through the items, printing their codes, names, and prices.
        print(f"{item['item_code']}| {item['item_name']} ----- AED {item['item_price']}")


def add_item_to_cart(code, item_list): #This function adds an item to the cart based on the provided item code. 
    for item in item_list: #It returns True if the item is found and added, and False otherwise.
        if code == item['item_code']:
            cart.append(item)
            print(f"\n{item['item_name']} has been added to your cart.")
            return True
    return False


def display_cart(): #This function displays the items in the cart
    print("\n-----------------------CART-----------------------\n")
    for c in cart: #The loop iterates through the items in the cart
        print(f"{c['item_name']} - AED {c['item_price']:.2f}")
    print("\n--------------------------------------------------")
    print("\nTotal ----------- AED", item_sum(cart)) #Shows the total cost of the items in the cart.
    print("\n--------------------------------------------------")


def item_sum(cart):
    return sum(item['item_price'] for item in cart) #This function calculates and returns the total cost of the items in the cart.

def process_purchase(): #This function handles the purchase process. 
    global run, money #the global keyword allows the function to modify the global variable instead of creating a local variable with the same name
    print(f"Your total is AED {item_sum(cart)}")

    inserted_money = float(input("Insert money: ")) #It prompts the user to insert money
    while inserted_money < item_sum(cart): #The loop checks for sufficient funds
        print("\nInsufficient Balance")
        additional_money = float(input("Insert more money: "))
        inserted_money += additional_money
        print(f'Your balance is AED {inserted_money}')

    money = inserted_money  # Update the global variable
    display_receipt() #calls/displays receipt
    dispense_items() #calls/dispenses items
    print('\nThank you for using the CanCake Pantry!')
    print('Have a GOOD DAY!')
    print("Don't forget your change")
    
def display_receipt(): #displays the receipt
    print("\nHere is your receipt:")
    print("\n------------------------------RECEIPT------------------------------\n")
    for c in cart: #for loop iterates through the items in cart
        print(f"{c['item_name']} ----------- AED {c['item_price']:.2f}")
    print("\n-------------------------------------------------------------------")
    print(f"\nTotal ----------- AED {item_sum(cart)}")
    print(f"Cash ----------- AED {money:.2f}")
    print(f"Change ----------- AED {max(0, money - item_sum(cart)):.2f}")  # Ensure change is non-negative
    print("\n-------------------------------------------------------------------")
    print("\nThank you for your purchase!\n")


def dispense_items(): #This function prints a message indicating that the purchased items have been dispensed.
    for c in cart:
        print(f'Your {c["item_name"]} has been dispensed')


def main(): #the main logic or code of the vending machine
    global run
    print("\n----------Welcome to the CanCake Pantry!----------")
    display_menu("Classic", item_classic) #displays menu
    print("\n--------------------------------------------------")
    display_menu("Special", item_special)
    print("\n--------------------------------------------------")
    display_menu("Drinks", item_drinks)
    print("\n--------------------------------------------------")
    run = True

    while run: #controls the main flow of the program
        while True: # handles user input and item code validation
            buy_item = input("\nEnter the code of the item you want to buy or press 'c' to cancel: ")

            if buy_item.lower() == 'c': #The inner loop breaks when a valid item is added to the cart or when the user cancels the purchase.
                print("\nPurchase canceled. Thank you for using the vending machine!")
                run = False
                break

            item_found = False
            for category, items_list in items.items():
                if add_item_to_cart(buy_item, items_list):
                    item_found = True
                    break

            if item_found:
                break
            else:
                print("\n----------INVALID CODE----------")

        if not run:
            break

        more_items = input("\nDo you want to buy more items? (yes/no): ")
        if more_items.lower() == 'no':
            print('\n')
            display_cart() #calls function
            process_purchase() #calls function
            run = False

main()