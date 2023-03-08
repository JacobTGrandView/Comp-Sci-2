# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 13:44:12 2021

@author: jt108
"""

def rev(mystring):
    if len(mystring) == 1:
        return(mystring)
    else:
        return rev(mystring[1:]) + mystring[0]

mystring = 'Jacob'
print(rev(mystring))