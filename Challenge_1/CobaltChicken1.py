#CobaltChicken,9/12,Challenge 1,Referenced in class powerpoints and TA


# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as mplot
import numpy as np
import csv

#open file break each line into a list of each value
with open('CobaltChicken_ch1.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    
#Creates xaxis list, yaxis list, CorrectFrequency list    
    xaxis=[]
    np.asarray(xaxis)
    yaxis=[]
    np.asarray(yaxis)
    Correct_Frequency=[]
    np.asarray(Correct_Frequency)
#Loops through csv file and if correct frequency append whole row to Correct_Frequency    
#If Correct Frequency, append timestamp to xaxis, and amplitude to yaxis   
    for row in reader:
        if float(row[2]) > 70.0:
           Correct_Frequency.append(row)
           xaxis.append(float(row[0]))
           yaxis.append(float(row[1]))
            
mean=0.0
count=0.0
TimeStamp=0.0
#Create ML to hold list of means
ML = []
np.asarray(ML)
#Create TS to hold list of TimeStamps 
TS=[]
np.asarray(TS)
TS.append(0.0)

#Loop through Correct_Frequency. If timestamp is 0, add all numbers to mean variable, count till Timestamp no longer = 0
for row in Correct_Frequency:
    if (TimeStamp == float(row[0])):
        count += 1
        mean += float(row[1])
#Now that TimeStamp is no longer = 0, move to else.    
    else:
#Calculate mean for each timestamp, and append to ML.        
        ML.append(mean/count)        
#reset count        
        count = 1
#Append Timestamp to TS.        
        TS.append(float(row[0]))
#old timestamp has been appended, set Timestamp to next value        
        TimeStamp = float(row[0])
#old tmean has been appended, set mean to next value        
        mean = float(row[1])

#Append timestamps mean
ML.append(mean/count)        
        

     




#Plot and design 
mplot.scatter(xaxis,yaxis, c = "blue")
mplot.plot(TS, ML, c = "red")

mplot.title('Challenge 1')
mplot.ylabel('Amplitude')
mplot.xlabel('Milliseconds')
mplot.show()
mplot.show()

