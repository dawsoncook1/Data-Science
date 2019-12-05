#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 16:57:00 2019

@author: dawsoncook
"""

"""

CobaltChicken, 11/4, challenge 4
Sources:
https://www.geeksforgeeks.org/python-string-isalpha-application/
https://stackoverflow.com/questions/189087/how-can-i-in-python-iterate-over-multiple-2d-lists-at-once-cleanly
T-A 
Lecture slides/old programs
"""


import numpy as np
import matplotlib.pyplot as mplot
import csv



userinp = input ("Enter a K value greater than 0: ")


if userinp.isalpha() or int(userinp) < 0:
    print("Please Enter an integer greater than 0! ")
else:
    x=[]
    y=[]
    x2=[]
    y2=[]
    z2=[]
    arrX=[]
    arrY=[]
    arrV=[]
    with open('us_outline.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        
        
        
       
        for row in reader:
            x.append(float(row[0]))
            y.append(float(row[1]))
          
 
    with open('data.csv', 'r') as csvfile2:
        
        reader2 = csv.reader(csvfile2, delimiter = ',')
        

    
        
        
        for row in reader2:
            x2.append(float(row[0]))
            y2.append(float(row[1]))
            z2.append(float(row[2]))
        
              
        
        
       
        for height in range(194):
            for width in range(120):
               
                dist=[]
                for col in range(len(x2)):
                    
                    dist.append([np.sqrt(np.power(x2[col] - height,2)+np.power(y2[col] - width,2)), col])
                dist.sort()
                print(z2)    
                avg=0.0
                for k in range(0, int(userinp)):
                   avg += z2[dist[k][1]]
                avg /= int(userinp)
                
                
                
                
                
                arrX.append(height)        
                arrY.append(width)
                arrV.append(avg)  
                    
                
        
            
                
     
    
    mplot.plot(x, y)
   
    mplot.scatter(arrX, arrY, c=arrV, cmap="viridis" )
    mplot.show()       
