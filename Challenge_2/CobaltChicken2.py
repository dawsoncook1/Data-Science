#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 11:55:15 2019

@author: dawsoncook
"""


"""
CobaltChicken, 9/29, challenge 2
Sources:
https://stackoverflow.com/questions/1801668/convert-a-python-list-with-strings-all-to-lowercase-or-uppercase    
https://www.geeksforgeeks.org/python-check-if-two-lists-are-identical/
https://www.geeksforgeeks.org/log-functions-python/
https://stackoverflow.com/questions/5843518/remove-all-special-characters-punctuation-and-spaces-from-string
https://pythonspot.com/matplotlib-bar-chart/
"""
import errno
import glob
import re
import csv
import math
import matplotlib.pyplot as plt
#function to find unique words in my list, and count of words
def L(listoflists, string):
    for row in listoflists:
        if row[0] == string:
            #print ("count")
            row[1] += 1
            return listoflists
        
            
    listoflists.append([string, 1])
    return listoflists
        
        

userinp = input ("Which file would you like to open? a or b: ")
if userinp == "a":
    path = 'a*.txt'
else:
    path = 'b*.txt'
files = glob.glob(path)
for name in files:
    try:
        with open(name) as f:
         listoflist = []
         words = []
         data = f.read()
         DS = data.split()
         Lowercase = []
         #chnages all words to lowercase
         ([Lowercase.append(i.lower()) if not i.islower() else Lowercase.append(i) for i in DS])
    
    #removes special charcters
         SCR = [re.sub("[^a-zA-Z' ]+", '', _) for _ in Lowercase]
         
         #Applies L function to SCR and creates list with unique word and count
        for word in SCR:
             listoflist=L(listoflist, word)
             for word in listoflist:
                 print(word)
                            
    
    
    except IOError as exc:
        if exc.errno != errno.EISDIR:
            pass
   


         
Neg = 0.0
WeakNeg = 0.0
Neutral = 0.0
WeakPos = 0.0
Pos = 0.0

#open csv and check conditions of lexicon and add count of correct lexicon to certain variable
with open('sentiment_lex.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    for row in reader:
        for word in listoflist:
            if (float(row[1]) < -0.6 and (row[0]) == word[0]):
                Neg += float(word[1])
            elif ((float(row[1]) > -0.6 and float(row[1]) < -0.2) and (row[0]) == word[0]):
                WeakNeg += float(word[1])
            elif ((float(row[1]) > -0.2 and float(row[1]) < 0.2) and (row[0]) == word[0]):
                Neutral += float(word[1])    
            elif ((float(row[1]) > 0.2 and float(row[1]) < 0.6) and (row[0]) == word[0]):
                WeakPos += float(word[1])
            if (float(row[1]) > 0.6 and (row[0]) == word[0]):
                Pos += float(word[1])
      


#Convert to log base 10
NegLog = math.log(Neg,10)
WeakNegLog = math.log(WeakNeg,10)
NeutralLog = math.log(Neutral,10) 
WeakPosLog = math.log(WeakPos,10)
PosLog = math.log(Pos,10) 

#plot
objects = ['Negative', 'WeaklyNegative', 'Neutral', 'WeaklyPositive', 'Positive']
listofcount = [NegLog,WeakNegLog,NeutralLog,WeakPosLog,PosLog]
plt.bar(objects, listofcount) 
plt.ylabel('Log Word Count')
plt.xlabel('Sentiment')
plt.title('Sentiment Analysis for series ' + userinp)
plt.show()    
        