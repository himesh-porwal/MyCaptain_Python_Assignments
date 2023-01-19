# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 19:45:05 2023

@author: Himesh Porwal

Program to print all the positive numbers in a range
"""
list1 = []
i= int (input("The number of elements in the list is: "))
print (" \nAdd the elements of list:")
j=0
while j<i:
    a= int(input())
    list1.append(a)
    j=j+1
    
print ("\nThe list is:",list1)
print ("\nThe positive numbers are:")

for x in list1:
    if (x>=0):
        print (x)
        
print ("\n\nDone!")
    