"""Register-machine"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

PRODUCTS = {}
EXISTENT = []
PRICE = []
CARDS = []


def reset():
    """This cleans the screen"""
    if os.name == "posix":
        os.system("clear")
reset()

def delete_lists():
    """This deletes the lists"""
    del EXISTENT[:]
    del PRICE[:]
    del CARDS[:]

def press_enter():
    """This says to the user press enter"""
    raw_input("\n\nPress Enter")

def product_isalpha(product):
    """This verifies the valid name of the product"""
    if product.isalpha():
        return True
    else:
        return False

def minuscule(product):
    """This converts the product in minuscule"""
    product = product.lower()
    return product

def valid_name():
    """This saves the name of the product"""
    reset()
    valid_product = False
    while valid_product == False:
        product = raw_input("Enter The product: ")
        product_lower = minuscule(product)
        valid_product = product_isalpha(product)
        if valid_product == False:
            print "Insert Valid Option please"
    return product_lower

def the_price():
    """This saves the price"""
    while True:
        price = raw_input("Enter the price: ")
        try:
            price = float(price)
            return price
        except ValueError:
            print "Insert only numbers"
    return price

def add_prod(product, price):
    """This saves the products and prices in a dictionary"""
    PRODUCTS[product] = price

def articles_with_price():
    """This adds the product with their respective price"""
    product = valid_name()
    price = the_price()
    add_prod(product, price)
    while True:
        other = raw_input("\nDo you want to insert other article? y/n ")
        other = other.lower()
        if other == "y":
            product = valid_name()
            price = the_price()
            add_prod(product, price)
        elif other == "n":
            reset()
            main_menu()
        else:
            reset()
            print "Insert only y/n please"

def product_sell():
    """This inserts the product to buy"""
    product = raw_input("\n - ")
    buy = minuscule(product)
    return buy

def done():
    """This verifies if the user not buys"""
    if EXISTENT == []:
        print "\nCan't generate the bill because You have not bought"
        press_enter()
        reset()
        show_products()
        sell_product()
    else:
        reset()
        bill()
        press_enter()
        delete_lists()
        reset()
        main_menu()

def sell_product():
    """This verifies if the product is available"""
    print "\nInsert the products you want to buy: "
    print "Press done to finish\n"
    while True:
        buy = product_sell()
        if PRODUCTS.has_key(buy) == True: 
            print "   Q%.2f " % (PRODUCTS.get(buy))
            EXISTENT.append(buy) 
            PRICE.append(PRODUCTS[buy])
        elif buy == "done":
            done()
            main_menu()
        elif buy == "gold":
            CARDS.append("gold")
        elif buy == "silver":
            CARDS.append("silver")
        else:
            print "\nThis product is not available"

def show_products():
    """This shows the products in sale"""
    print "These are the products in sale"
    for key, value in PRODUCTS.iteritems():
        print "%s: Q%.2f" % (key, value)

def ask_of_user():
    """This asks to the user if wants to see the products"""
    while True:
        question = raw_input("Do you want to see the products in sale? y/n ")
        question = question.lower()
        if question == "y":
            reset()
            show_products()
            sell_product()
        elif question == "n":
            reset()
            sell_product()
        else:
            print "Election invalid"

def dic_next():
    """Verifies if the dictionary is empty"""
    if PRODUCTS == {}:
        print "\n**No products availabe**" 
        press_enter()
        reset()
        main_menu()
    else:
        ask_of_user()

def list_of_products(list_products):
    """This counts each item"""
    for each_product in PRODUCTS:
        num_prudcts = list_products.count(each_product) 
        if num_prudcts > 0:
            price = PRODUCTS[each_product]
            print num_prudcts, each_product + "(s)", "a", ("Q%.2f c/u") % price

def gold_card(subtotal):
    """This calculates the discount of the gold card"""
    return subtotal * 0.05

def silver_card(subtotal):
    """This calculates the discount of the silver card"""
    return subtotal * 0.02

def my_subtotal():
    """This adds all the prices"""
    return sum(PRICE)

def discount_of_cards(subtotal):
    """This verifies the discount of the card"""
    if "gold" in CARDS:
        return gold_card(subtotal)
    elif "silver" in CARDS:
        return silver_card(subtotal)
    elif "gold" in CARDS and "silver" in CARDS:
        return gold_card(subtotal)
    else:
        return 0 

def tax(subtotal, discount):
    """This calculates the IVA"""
    return (subtotal - discount) * 0.12

def my_total_final(subtotal, discount, iva):
    """This calculates the total final"""
    return (subtotal - discount) + iva

def bill():
    """This prints the bill"""
    subtotal = my_subtotal()
    discount = discount_of_cards(subtotal)
    iva = tax(subtotal, discount)
    total = my_total_final(subtotal, discount, iva)
    reset()
    list_of_products(EXISTENT)
    print "\nThe subtotal is:----------- Q%.2f" % subtotal
    print "The discount is:----------- Q%.2f" % discount
    print "The tax is:---------------- Q%.2f" % iva
    print "The total to pay is:------- Q%.2f" % total
    print "-------------------------------------"
    print "\n\n---Thank you for shopping with us---"

def main_menu():
    """This saves the main menu"""
    print "__________________________________"
    print " Welcome to the Register Machine  "
    print "       1. Add and Item            "
    print "       2. Sell Articles           "
    print "       3. Exit                    "
    print "__________________________________"
    answer = True
    while answer == True:
        enter = raw_input(" - ")
        if enter == "1":
            reset()
            articles_with_price()
        elif enter == "2":
            reset()
            dic_next()
        elif enter == "3":
            reset()
            sys.exit() 
        else:
            reset()
            print "*Election invalid, choose a valid option"
            main_menu()

if __name__ == "__main__":
    main_menu()
