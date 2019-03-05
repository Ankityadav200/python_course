# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 17:44:25 2019

@author: ankit
"""

#calculate the area and parameter of the circle by taking input  by user
import math
dir(math)
help(math.pi)
from math import pi

radius=int(input("radius of the circle:"))
print(radius)
 
area_of_circle=pi*radius*radius
#Pi=3.14
print(area_of_circle)
 
parameter_of_cir=2*pi*radius
print(parameter_of_cir)