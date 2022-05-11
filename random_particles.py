# -*- coding: utf-8 -*-
"""
Created on Wed May  4 17:17:20 2022

@author: shree_codes
"""

# of randint() function
# imports random module

#for loop
import random 

#For 40 particles total
l = 0
u = 40
for num in range (l, u):
    
    r1 = random.uniform(0,20)
    print("C % s" % (r1), end =" ")
    
    r2 = random.uniform(0,20)
    print(" % s" % (r2), end =" ")
    
    r3 = random.uniform(0,20)
    print(" % s" % (r3))
    
    
    
