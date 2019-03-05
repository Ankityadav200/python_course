# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 16:24:06 2019

@author: ankit
"""

#take first and last name in single command from the user and print them in reverse order with space betwwen them
first,last=input("enter your first name:"),input("enter your last name:")
print ("The full name in reverse:{} {}".format(last,first))

new=first+" "+last
print("the full name is :",new)
s=new.index(' ')
print(s)
string=new[s:]+" "+new[:s]
print("the full name after slicing is:",string)