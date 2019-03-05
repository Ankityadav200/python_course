# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 17:45:06 2019

@author: ankit
"""

# The computer will think of a random number from 1 to 10 as secret number
import random
secret_no=random.randint(0,10)

#Then ask you ( Player ) to guess the number and store as guess number Compare the guess number with the secret number 

gues_no=int(input("enter the no:"))

if(secret_no==gues_no):
    print("player win and computer loses")
else:
        print("player lose and computer wins")
        print("The guess no is {} and the secret no is {}".format(gues_no,secret_no))