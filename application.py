"""REGISTER MACHINE"""

#!/usr/bin/env python
# -*- coding: utf-8 -*

import os
import sys

PRODUCTS = {} #This saves the products added
EXISTENT = [] #This saves the products existent
PRICE = [] #This saves the prices of the products
CARDS = [] #This saves the credits cards


def clear():
    """THIS CLEANS THE SCREEN"""
    if os.name == "posix":
        os.system("clear")
    elif os.name == ("nt",):
        os.system("cls")
clear()

def press_enter():
    """THIS SAYS TO THE USER PRESS ENTER"""
    raw_input("\n\nPress ENTER button to return to main menu")

#Test 1 produc_isalpha
def product_isalpha(product):
    """THIS VERIFIES THE VALID NAME OF THE PRODUCT"""
    if product.isalpha(): #this verifies if the product entered is alphabetic
        return True
    else:
        return False

def delete_lists():
    """THIS DELTES THE LISTS"""
    del EXISTENT[:]
    del PRICE[:]
    del CARDS[:]

#Test 2 minuscule
def minuscule(product):
    """THIS CONVERTS THE PRODUCT IN MINUSCULE"""
    product = product.lower()
    return product

def add_prod(product, price):
    """THIS SAVES THE PRODUCTS AND PRICES IN A DICTIONARY"""
    PRODUCTS[product] = price

def valid_name():
    """THIS SAVES THE NAME OF THE PRODUCT"""
    clear()
    valid_product = False
    while valid_product == False:
        product = raw_input("\n--Enter The product: ") #This asks entered the product
        product_lower = minuscule(product)
        valid_product = product_isalpha(product)
        if valid_product == False:
            print "\nInsert Valid Option please"
    return product_lower

def the_price():
    """THIS SAVES THE PRICE"""
    while True:
        price = raw_input("\n--Enter the price: ") #This asks entered the pice
        try:
            price = float(price)
            return price
        except ValueError:
            print "\nInsert only numbers please"
    return price

def articles_with_price():
    """THIS ADDS THE PRODUCT WITH THEIR RESPECTIVE PRICE"""
    product = valid_name()
    price = the_price()
    add_prod(product, price)
    while True:
        other = raw_input("\nDo you want to insert other article? yes/no: ")
        other = other.lower()
        if other == "y" or other == "yes":
            product = valid_name()
            price = the_price()
            add_prod(product, price)
        elif other == "n" or other == "no":
            clear()
            main_menu()
        else:
            print "\nInsert only yes/no please"

def product_sell():
    """THIS INSERTS THE PRODUCT TO BUY"""
    product = raw_input("\n -- ") #asks the user to enter the product
    buy = minuscule(product)
    return buy

def sell_product():
    """THIS VERIFIES IF THE PRODUCT IS AVAILABLE"""
    print "\nInsert the products you want to buy: "
    print "Press done to finish\n"
    while True:
        buy = product_sell()
        if PRODUCTS.has_key(buy) == True: #Verifies if the product belongs to the dictionary
            print "   Q%.2f " % (PRODUCTS.get(buy)) #this shows the price of the product
            EXISTENT.append(buy)
            PRICE.append(PRODUCTS[buy]) #This saves the price
        elif buy == "done":
            done()
            main_menu()
        elif buy == "gold":
            CARDS.append("gold") #This adds the gold card
        elif buy == "silver":
            CARDS.append("silver") #This adds the silver card
        else:
            print "\nThis product is not available"

def done():
    """THIS VERIFIES IF THE USER NOT BUYS"""
    if EXISTENT == []:
        print "\nError has not made a purchase"
        press_enter()
        clear()
        sell_product()
    else:
        clear()
        bill()
        press_enter()
        delete_lists()
        clear()
        main_menu()

def dic_next():
    """VERIFIES IF THE DICTIONARY IS EMPTY"""
    if PRODUCTS == {}: #checks whether there is products available
        print "\nThere is no products to show"
        press_enter()
        clear()
        main_menu()
    else:
        sell_product()

def list_of_products(list_products):
    """THIS COUNTS EACH ITEM"""
    for each_product in PRODUCTS:
        num_prudcts = list_products.count(each_product) #This count each product
        if num_prudcts > 0:
            price = PRODUCTS[each_product]
            print num_prudcts, each_product + "(s)", "a", ("Q%.2f c/u") % price

#Test3 Gold Card
def gold_card(subtotal):
    """THIS CALCULATES THE DISCOUNT OF THE GOLD CARD"""
    return subtotal * 0.05

#Test4 Silver Card
def silver_card(subtotal):
    """THIS CALCULATES THE DISCOUNT OF THE SILVER CARD"""
    return subtotal * 0.02

def my_subtotal():
    """THIS ADDS ALL THE PRICES"""
    return sum(PRICE)

def discount_of_cards(subtotal):
    """THIS VERIFIES THE DISCOUNT OF THE CARDS"""
    if "gold" in CARDS:
        return gold_card(subtotal)
    elif "silver" in CARDS:
        return silver_card(subtotal)
    elif "gold" in CARDS and "silver" in CARDS:
        return gold_card(subtotal)
    else:
        return 0

#Test5 tax
def tax(subtotal, discount):
    """THIS CALCULATES THE IVA"""
    return (subtotal - discount) * 0.12

#Test6 My Total Final
def my_total_final(subtotal, discount, iva):
    """THIS CALCULATES THE TOTAL FINAL"""
    return (subtotal - discount) + iva

def bill():
    """THIS PRINTS THE BILL"""
    subtotal = my_subtotal() #This verifies the subtotal of the buy
    discount = discount_of_cards(subtotal) #This verifies the discount of the buy
    iva = tax(subtotal, discount) #This verifies the iva of the buy
    total = my_total_final(subtotal, discount, iva) #This verifies the total final of the buy
    clear()
    list_of_products(EXISTENT)
    print "\n------------------------------------"
    print "The subtotal is:            Q%.2f  " % subtotal
    print "The discount is:            Q%.2f  " % discount
    print "The tax is:                 Q%.2f  " % iva
    print "The total to pay is:        Q%.2f  " % total
    print "--------------------------------------"
    print "\n\n---Thank you for your purchase!!---"
    print "        ---Come back soon---           "

def main_menu():
    """THIS SHOWS THE MAIN MENU"""
    print "___________________________________"
    print "| Welcome to the Register Machine  |"
    print "|       1. Add an Item             |"
    print "|       2. Sell Articles           |"
    print "|       3. Exit                    |"
    print "|__________________________________|"
    answer = True
    while answer == True:
        enter = raw_input("\n -- ")
        if enter == "1":
            clear()
            articles_with_price()
        elif enter == "2":
            clear()
            dic_next()
        elif enter == "3":
            clear()
            sys.exit()
        else:
            print "\nInvalid Option"

if __name__ == "__main__":
    main_menu()
