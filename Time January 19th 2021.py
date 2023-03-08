# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 13:24:01 2021

@author: jt108
"""

import time


def sum_of_n_2(n):
    start = time.time()
    
    the_sum = 0
    for i in range(1, n + 1):
        the_sum = the_sum + i
        
    end = time.time()
    
    return the_sum, end - start