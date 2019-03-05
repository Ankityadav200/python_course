# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 17:15:03 2019

@author: ankit
"""

# Catch when someone submits a non integer
import random

secret_no=random.randint(0,10)

while(True):
    guess_no=input("enter the number:")
    dt=(type(guess_no))
    if(dt!=int):
        print("it is a non integer")
    else:
        if(guess_no==secret_no):
            print("player wins")
            break
        else:
            print("player lose")