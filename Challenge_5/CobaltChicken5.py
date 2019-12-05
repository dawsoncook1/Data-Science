#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 18:48:13 2019

@author: dawsoncook

CobaltChicken, 11/18, challenge 5
Sources:
https://pythonprogramming.net/how-to-program-best-fit-line-machine-learning-tutorial/
https://stackoverflow.com/questions/5056064/element-that-appear-more-that-once-in-the-list-in-python
https://stackoverflow.com/questions/42512346/python-average-distance-between-a-bunch-of-points-in-the-x-y-plane
"""

import numpy as np
import matplotlib.pyplot as mplot
import csv
import math
from itertools import combinations

def dist(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


freq=[]

uniq_freq=[]

with open('CobaltChicken.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    
    
    for row in reader:
        freq.append(float(row[1]))
    
    for x in freq:
        if x not in uniq_freq:
            uniq_freq.append(x)
    
for val in uniq_freq:
    
    
    #x and y list here so resets for each freq
    x=[]
    y=[]
    avg_avg=0.0
    with open('CobaltChicken.csv', 'r') as csvfile:
        reader2 = csv.reader(csvfile, delimiter = ',')
        for row in reader2:
            if val == float(row[1]):
                x.append(float(row[0]))
                y.append(float(row[2]))
    
    mplot.scatter(x, y)        
    #find actual data and if actual then do math. If dots are close together than actual. nearest neighbor? if val is less than avg distance then actual
    points = zip(x,y)
    
    
    distances = [dist(p1, p2) for p1, p2 in combinations(points, 2)]
    
    
    #find the avg dustance of each freq
    avg_distance = np.array(sum(distances)) / np.array(len(distances))
    
    a = [avg_distance]
    b=np.array(a)
    b= np.mean(avg_distance)
    
    
   
    
    if avg_distance < 70.0:
        
        meanx=np.mean(x)
        meany=np.mean(y)
        
        corr=np.corrcoef(x, y)
        
        temp=corr[0][1]
        standev_x=np.std(x)
        standev_y=np.std(y)
        
    
       
        slope=(standev_y * temp)/standev_x
        
    
    
        b=(meany-(meanx*slope))
        #regression_line list here so resets for different slopes
        regression_line=[]
        for point in x:
            regression_line.append((slope*point)+b)
            
        params=np.polyfit(x, y, 3)
    
        #new range of x-values to test
        xnew=np.float32(range(0, 1000))
        xnew=xnew/10.0
    
        #generates the predicted y-values
        ypred=np.polyval(params, xnew)
    
        #make a line plot of our predicted data
        mplot.plot(xnew, ypred)
        mplot.plot(x, regression_line)
        
mplot.show()


