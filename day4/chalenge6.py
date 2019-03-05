# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 15:22:53 2019

@author: ankit
"""
#Challenge 6
    #Print the number of tries left 
import random
secret_no=random.randint(0,10)



gues_no=int(input("enter the no:"))


n=1
while(n<6):
    print(n)
    print("number of tries left:",6-n)
    n=n+1
     if(gues_no!=secret_no):
         gues_no=int(input("enter the no:"))
         else:
             print("player wins")
             print("the secret no",secret_no)
             break