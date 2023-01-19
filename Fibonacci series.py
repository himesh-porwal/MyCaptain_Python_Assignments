# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 20:12:35 2023

@author: Himesh Porwal

Fibonacci series
"""
n= int(input("Enter the number of terms: "))
print("The fibonacci series is:")
i=0
j=1
if(n<=0):
    print ("Invalid number")
else:
    a=1
    while (a<=n):
        print(i)
        k=i+j
        i=j
        j=k
        a=a+1