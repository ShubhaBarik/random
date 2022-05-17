# -*- coding: utf-8 -*-
"""
Created on Tue May 17 13:54:56 2022

@author: shree
"""

import math

def comp_dist(a,b):
    #a = [r1, r2, r3] --> pos1
    #b = list of all atom positions
    #returns the dist b/w all the atoms of a and b
    empty_list = [] #create an empty list
    #extracting each x y z value of pos1 (contained in a)
    for i in a:
        x1 = a[0]
        y1 = a[1]
        z1 = a[2]        
    
    #extracting each x y z values of all the positions (contained in b)
    for i in b:
        x2 = b[0]
        y2 = b[1]
        z2 = b[2]
    
    return distance = math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2) + math.pow(z2-z1,2) * 1.0)
    print("Distance= ", distance)
    empty_list.append(distance)
    
#len_b = len(b)
#for i in range(0,len_b):
    

if dist < 4
