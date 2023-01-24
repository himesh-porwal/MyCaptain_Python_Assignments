# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 06:28:56 2023

@author: Himesh Porwal

Program to print the frequency of letters in a word in descending order
"""
dict1= {}
def most_frequent(string):
    for x in string:
        if x not in dict1:
            dict1[x]=1
        else:
            dict1[x]=dict1[x]+1
most_frequent(input("Enter a word in one single case: "))

sorted_values = sorted(dict1.values(),reverse=True) # Sort the values 
sorted_dict = {}  


for i in sorted_values:     
    for k in dict1.keys():         
        if dict1[k] == i:             
            sorted_dict[k] = i             
print(sorted_dict)