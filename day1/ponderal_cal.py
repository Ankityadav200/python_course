# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 16:07:26 2019

@author: ankit
"""

#bmi of my body is 14
bmi_value=float(input("bmi of my body:"))
print(bmi_value)

#my height in meter 
height_inmeter=float(input("my height in meter:"))
print(height_inmeter)

# calculate ponderal value of person
ponderal_index=(bmi_value/height_inmeter)
print(ponderal_index)

roundof_ponderalvalue=round(ponderal_index)
print(roundof_ponderalvalue)
