# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 16:45:54 2019

@author: ankit
"""
#hands on
string="Animation"
#prints the characters at the even index number
print(string[1:10:2])

#hands on 2
string="Animation"
#print the given string in reverse
print(string[::-1])

#handson 3
string="Forsk Technologies"
#print forsk using slicing(forward indexing left to right)
print(string[0:5])

#hands on 4
string="Forsk Technologies"
#printing technologies using slicing (forwarding left to right)
print(string[6:])


#hands on 5
string="Forsk Technologies"
#print forsk using slicing reverse(right to left)
print(string[-18:-13])
#hands on 6
string="Forsk Technologies"
#hands on 7
string="Forsk Technologies"
#print technologies using slicing reverse(right to left)
print(string[-13:-0])
#hands on 8
string="Forsk Technologies"
#print siesgolonhcet using slicing(forward indexing left to right)
print(string[-1:-13:-1])
#hands on 9
string= "Forsk Technologies"
#print technologies forsk using slicing(forward indexing left to right)
print(string[6:20] + " " + string[0:5])
#hands on 10
string="Forsk Technologies"
#print technologies forsk using slicing (reverse right to left)
print(string[-12] + " " +
string[-20:-13])