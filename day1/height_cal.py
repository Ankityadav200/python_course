# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 14:40:07 2019

@author: ankit
"""

#my present height is 5 foot and 11 inches
foot=5
inch=11
print(foot,inch)
my_height=(foot,inch)
print(my_height)

#converting foot into meters
new_foot=foot*0.3048

#converting inch into meter
new_inch=inch*0.0254
print(new_foot)
print(new_inch)
# my height in meters
total_height_meter=(new_foot+new_inch)
print(total_height_meter)

# convert foot in centimeters
new_cent_foot=new_foot*100
print(new_cent_foot)
#convert inch into cdentimeter
new_cent_inch=new_inch*100
print(new_cent_foot,new_cent_inch)
#total height in centimeters
total_heightin_cent=(new_cent_foot+new_cent_inch)
print(total_heightin_cent)