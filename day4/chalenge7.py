# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 15:28:48 2019

@author: ankit
"""
#challenge7
#Lets give user the option to play again
import random
secret_no=random.randint(0,10)
i=input("do you want to play again (Y/N):")
while(i!="N"):
    if (i=='Y'):
        gues_no=int(input("enter the no:"))
        if(gues_no==secret_no):
            print("player wins")
            break
        else:
            print("player lose:")
        i=input("do you want to play again (Y/N):")
