# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 17:51:32 2019

@author: ankit
"""

# Print too HIGH or too LOW messages for bad guesses using elif. 

import random
secret_no=random.randint(0,10)

#Then ask you ( Player ) to guess the number and store as guess number Compare the guess number with the secret number 

gues_no=int(input("enter the no:"))

if(secret_no==gues_no):
    print("player win and computer loses")
elif(secret_no>gues_no):
        print("too low")    
else:
        print("too high")
        
        
    