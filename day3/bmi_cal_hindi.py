# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 17:06:11 2019

@author: ankit
"""

#my weight in kilogram 
my_weight_inkg=float(input("किलो में वजन:"))
print(my_weight_inkg)

#my height in meteres
height_inmeter=float(input("मीटर में ऊँचाई:"))
print(height_inmeter)

#calculate bmi of body
bmi_value=(my_weight_inkg/height_inmeter)
print(bmi_value)

#divide the bmi value with height

new_bmi=(bmi_value/height_inmeter)
print(new_bmi)
