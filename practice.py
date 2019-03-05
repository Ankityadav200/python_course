# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:14:17 2019

@author: ankit
"""

age=int(input("enter the age:"))    
print(age)
if(age>=0 and age<=1):
    print("infant")
elif(age>1 and age<=18):
    print("child");
elif(age>18 and age<=60):
    print("adult");    
else:
    print("senior citizion");
    
