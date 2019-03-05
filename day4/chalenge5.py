# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 15:17:45 2019

@author: ankit
"""

#Challenge 5
#Limit the number of guesses to maximum 6 tries 
import random
secret_no=random.randint(0,10)


gues_no=int(input("enter the no:"))

n=1
while(n<6):
    
    n=n+1
    if(gues_no!=secret_no):
        gues_no=int(input("enter the number:"))
    else:
        print("player wins")
        print("the secret no",secret_no)
        break