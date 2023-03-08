# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 13:10:15 2021

@author: jt108
"""


"""

import time

l = []

init = time.time_ns()/1000000

for i in range(10000):
    l = l + [i]
    
final = time.time_ns()/1000000

print("time (ms) : ", (final - init))


"""


import time

init = time.time_ns()/1000000

l = []

for i in range(10000):
    l.append(i)
    
final = time.time_ns()/1000000

print("time (ms) : ", (final - init))
