# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 12:10:11 2021

@author: jt108
"""

def fact(num):
    if num < 2:
        return 1
    else:
        return num * fact(num-1)

num = int(input("Enter a number: "))
print(fact(num))