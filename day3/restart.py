# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 13:24:51 2019

@author: ankit
"""

#in hardcoded string RESTART ,replace all the R with$ except the first
dir(str)
help(str.replace)

newstr="RESTART"
newstr1 = newstr.replace("R","$")
 char=newstr[0]
 
 newstr1=char + newstr1[1:]
 print(newstr1)


