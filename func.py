# -*- coding: utf-8 -*-
"""
Created on Tue May 17 13:54:56 2022

@author: shree_codes
"""
import random
import math

l = 0
u = 40
for num in range (l, u):
    
    r1 = random.uniform(0,20)
    #print("C % s" % (r1), end =" ")
    
    r2 = random.uniform(0,20)
    #print(" % s" % (r2), end =" ")
    
    r3 = random.uniform(0,20)
    #print(" % s" % (r3))
    
    atom1 = [r1, r2, r3]

def comp_dist(a,b):
    #a = [r1, r2, r3] --> pos1
    #b = list of all atom positions
    #returns the dist b/w all the atoms of a and b
    empty_list = [] #create an empty list
    #extracting each x y z value of pos1 (contained in a)
    x1 = a[0]
    y1 = a[1]
    z1 = a[2]        
    
    #extracting each x y z values of all the positions (contained in b)
    for i in b:
        x2 = i[0]
        y2 = i[1]
        z2 = i[2]
    
        distance = math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2) + math.pow(z2-z1,2) * 1.0)
        #print("Distance= ", distance)
        empty_list.append(distance)
    return empty_list
  
a = [1, 2, 3] 
b = [[1, 2, 3], [3, 3, 3], [1, 5, 3]]
result = comp_dist(a,b)
#print("result: ", result)


def grt_no(distance,min_dist_val):
    #distance --> all the values of dist calculated
    #min_dist_val --> minimum dist value should be >=4
    #print(min_dist_val)   
    rv = True
    for i in distance:
        if i < min_dist_val:
            rv = False
    return rv
    

ans = grt_no([1.2, 5.3, 9.4, 6.3], 4)
#print("ans: ", ans)

###################################################
atomcoord = []
min_dist_val = 4
N = 40

while len(atomcoord) < N:
    r1 = random.uniform(0,20) #X
    
    r2 = random.uniform(0,20) #Y
    
    r3 = random.uniform(0,20) #Z
   
    newpos = [r1, r2, r3]
    result = comp_dist(newpos,atomcoord)
    if grt_no(result,min_dist_val):
        atomcoord.append(newpos)
print(atomcoord)

###################################################   


#len_b = len(b)
#for i in range(0,len_b):
    
#condition check
####else:
        
