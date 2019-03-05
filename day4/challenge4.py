# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 15:13:07 2019

@author: ankit
"""

#Challenge 4
  #  Let people play again and again until he guesses the right secret number
import random
secret_no=random.randint(0,10)

gues_no=int(input("enter the no:"))

while(True):
    print("player wins")
    print("secret number:",secret_no)
    break
else:
    gues_no=int(input("enter the no:"))