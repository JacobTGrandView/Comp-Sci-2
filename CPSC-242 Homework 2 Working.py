# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 13:29:04 2021

@author: jt108
"""

############
#
#Homework 2. Jacob Thomas. CPCS-242. 1/29/2021
#
############


#Part 1. Test if 2 complex numbers are equal, add 2 complex
#numbers, multiply 2 complex numbers, & divide 2 complex numbers

#1.13. Object-Oriented Programming in Python: Defining Classes
#In the online textbook!!!

#Have to combine real part with real part and imaginary with imaginary

#self is the reference back to the object



class Complex(): #class is like the blueprint

    def __init__(self, real, imaginary): #__init__ is constructor function
        self.real = real #makes real
        self.imaginary = imaginary #makes imaginary 

    def __add__(self, complex): #addition function for classes
        return Complex(self.real + complex.real, self.imaginary + complex.imaginary) #Add real numbers together and then imaginary numbers
    
    def __mul__(self, complex): #multiplication function
        return Complex((self.real * complex.real) - (self.imaginary * complex.imaginary),(self.imaginary * complex.real) + (self.real * complex.imaginary)) #FOIL, multiplying first, outside, inside, and then last

    def __truediv__(self, complex):
        j = (complex.real ** 2 + complex.imaginary ** 2)  #i squared. i^2 = -1. **  = exponent
        return Complex((self.real * complex.real - self.imaginary * complex.imaginary) / j ,(self.imaginary * complex.real + self.real * complex.imaginary) / j)
#mulitply by opposite recriprocal for denom and numerator, combine like terms
    def __str__(self): #return string representation of the object
        return str(self.real) + "+" + str(self.imaginary)+ "i" #adding i to the imaginary end of number and + to link them together


a = Complex(1, 2) #First number is real, 1, second number is imaginary, so 2
b = Complex(3, 4) #First number is real, 3, second number is imaginary, 4


print("Sum = ", str(a + b)) #Printing sum converted to string 
print("Multiplication = ", str(a * b)) #printing multiplication
print("Division = ", str(a / b)) #printing division








