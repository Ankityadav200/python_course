# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 16:23:35 2019

@author: ankit
"""

#let assume my age is 21
my_age=21
print(my_age)

#calculate the mximum heart rate
max_heartrate=my_age-220
print(max_heartrate)

#lower end of target heart rate is 70% of maximum heart rate

lr_rate=max_heartrate*0.70
print(lr_rate)

#higher end of target heart is 85% of maximum heart rate
 
hr_rate=max_heartrate*0.85
print(hr_rate)

#heart rate of a person 
heart_rate=("heart rate is"+str(lr_rate)+"to"+str(hr_rate)+" beats per minute")
print(heart_rate)