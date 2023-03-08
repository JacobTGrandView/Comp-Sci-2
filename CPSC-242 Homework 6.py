# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 20:08:18 2021

@author: jt108
"""

#Jacob Thomas. 3/26/2021. CPSC-242. Homework 6.


#Problem 3. #Write a recursive version of binary search 
            #by passing the indices as arguments
            
#I used the code on the slides and tried modifying it
            
            
def binary_using_indices(a_list, startindex, endindex, item): #list, starting point, ending point, the item being found
    middle = (startindex + endindex) // 2 #divide by 2 to get middle. Won't be a decimal because of //
    
    if a_list[middle] == item: #if the middle of the list is equal to the item return true
        return True
    
    
    elif(item < a_list[middle]): #item less than middle, return the values between starting index and the middle - 1 since it did not match the item
        return binary_using_indices(a_list, startindex, middle - 1, item)  
    else:
        return binary_using_indices(a_list, middle + 1, endindex, item)
    #If the item is greater than the middle, return the middle + 1 since it did not match and the values between end index


a_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14] #list of numbers
print(binary_using_indices(a_list, 0, 13, 4)) #printing function. Starts at index 0
                                              #ends at index 13. Searching for a 4





#problem 5. Hashing for a list of words.
#Words = {moose, elephant, viper, tarantula, baboon, tiger, jaguar}
#The rest of the work is in the word doc since it looks a lot nicer

#Making a list of what every letter is equal to
"""
print("a is equal to ", ord("a"))
print("b is equal to ", ord("b"))
print("c is equal to ", ord("c"))
print("d is equal to ", ord("d"))
print("e is equal to ", ord("e"))
print("f is equal to ", ord("f"))
print("g is equal to ", ord("g"))
print("h is equal to ", ord("h"))
print("i is equal to ", ord("i"))
print("j is equal to ", ord("j"))
print("k is equal to ", ord("k"))
print("l is equal to ", ord("l"))
print("m is equal to ", ord("m"))
print("n is equal to ", ord("n"))
print("o is equal to ", ord("o"))
print("p is equal to ", ord("p"))
print("q is equal to ", ord("q"))
print("r is equal to ", ord("r"))
print("s is equal to ", ord("s"))
print("t is equal to ", ord("t"))
print("u is equal to ", ord("u"))
print("v is equal to ", ord("v"))
print("w is equal to ", ord("w"))
print("x is equal to ", ord("x"))
print("y is equal to ", ord("y"))
print("z is equal to ", ord("z"))
"""

#the ord values combined

moose = 547
elephant = 849
viper = 550
tarantula = 972
baboon = 625
tiger = 539
jaguar = 634

"""
print(547 % 4)
print(849 % 4)
print(550 % 4)
print(972 % 4)
print(625 % 4)
print(539 % 4)
print(634 % 4)



print(547 % 18)
print(849 % 18)
print(550 % 18)
print(972 % 18)
print(625 % 18)
print(539 % 18)
print(634 % 18)
"""