# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 21:58:33 2021

@author: jt108
"""

def print_menu():
    print('1. Print Phone Numbers')
    print('2. Add a Phone Number')
    print('3. Remove a Phone Number')
    print('4. Quit')
    print()

numbers = {}
menu_choice = 0
print_menu()
while menu_choice != 4:
    menu_choice = int(input("Type in a number (1-4): "))
    if menu_choice == 1:
        print("Telephone Numbers:")
        for x in numbers.keys():
            print("Name: ", x, "\tNumber:", numbers[x])
        print()
    elif menu_choice == 2:
        print("Add Name and Number")
        name = input("Name: ")
        phone = input("Number: ")
        numbers[name] = phone
    elif menu_choice == 3:
        print("Remove Name and Number")
        name = input("Name: ")
        if name in numbers:
            del numbers[name]
        else:
            print(name, "was not found")
    elif menu_choice != 4:
        print_menu()