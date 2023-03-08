# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:15:18 2021

@author: jt108
"""

#Jacob Thomas. CPSC-242. 1/5/21. Homework #3




#Part 1. Finding smallest number in list. Find T(n) and upper bound


'''
def Smallest_Integer(): #function for finding smallest number

    list1 = [] #empty list to input numbers

    while(True): #infinite loop
        input1 = input("enter numbers one at a time or 'done' to stop: ")
    
        if(input1 == "done"): #if 'done' is entered, it stops
            break
    
        list1.append(int(input1)) #appends input numbers into list1
        
        list1.sort() #sorts from smallest to largest
        
    print("Smallest integer in list is: ", list1[0]) #prints whatever is in index 0 of list1
        
    
Smallest_Integer() #calling the function


#list1 = 1
#while loop = n
#if statement = 1 because 'done' is only entered once
#T(n) = n + 1
#T(n) = O(n) because the list could be infinite and the + 1 will no longer matter
'''





#Part 2. 2 numbers in a list that add up to 25. 


'''

def SumOf25(list1):
    
   
    Target = 25 #find two numbers that equal 25
    Target = False
    i = 0
    j = 0
    
    
    while(Target == False):
        i = i + 1
        
        while(Target == False):
            
            if i + j == 25:
                Target = True
                return(list1[i] + list1[j])
            
print(SumOf25([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
                
'''          



"""
def SumOf25(list1):
    i = 0
    j = 0
    Target = 25
    
    while(i < len(list1)):
        i = i + 1
        while(j < len(list1)):
            j = j + 1
    
        if(list1[i] + (list1[j] == Target)):
            print(i + j)
            
            
print(SumOf25([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
"""


"""
target = 25
List2 = []


while(True):
    input1 = input("enter numbers one at a time or 'done' to stop: ")
    
    if(input1 == "done"): #if 'done' is entered, it stops
        break
    List2.append(input1)

    for i in range((List2)):
        i = 0
        for j in range(List2):
            j = i + 1
            if(target == List2[i] + List2[j]):
                print(target)
"""



"""
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def SumOf25(list1):
    i = 0
    j = 0
    target = 25
    target = False
    
    while(i < len(list1)):
        i = i + 1
        while(j < len(list1)):
            if(target == True):
                print(list1[i] + list1[j])
                
SumOf25(list1)

"""
                
                
                