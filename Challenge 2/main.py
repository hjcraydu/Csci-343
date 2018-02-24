#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 22:13:09 2017

@author: Hailey Cray-Dubaz
Spirit Animal: Yellow Butterfly
Last Edited: 9/26/17
Challenge #3

Code taken from Lecture 8 
Code taken from Lecture 2
Received help from Paul Gardner
"""
from __future__ import division
import re #imports regular expression of python
import matplotlib.pyplot as mplot
import numpy as np

#lexicon
file=open("lexicon.csv", "r")
lexicon=file.read()
lexicon=lexicon.replace(",", " ")
lexicon=lexicon.split("\n")

userInput = raw_input("Enter file name: ")

file=open(userInput, "r")
data=file.read()
data=re.sub(r'\W+', ' ', data)
data=data.lower()
data=data.split(" ")

newDict={}
for line in lexicon:
     line=line.split(" ")
     try:
         
         newDict[line[0]]=np.float32(line[1])
     except:
        print("")

words={}
for word in data:
     try:
         words[word]=words[word]+1
     except:
         words[word]=1

ct_dict={}
for key, value in words.items():
     if key in newDict:
         ct_dict[key] = value

weak_pos=0
pos=0
weak_neg=0
neg=0
neut=0

for key, va in ct_dict.items():
    if key in newDict:
        if newDict[key] >= -1.0 and newDict[key] < -0.6:
            neg += va
            
        elif newDict[key] >= -0.6 and newDict[key] < -0.2:
            weak_neg += va
         
        elif newDict[key] >= -0.2 and newDict[key] <= 0.2:
            neut += va
     
        elif newDict[key] > 0.2 and newDict[key] <= 0.6:
            weak_pos += va
      
        elif newDict[key] > 0.6 and newDict[key] <= 1.0:
            pos += va 

total = neg + weak_neg + neut + weak_pos + pos

percent=[(neg/total), (weak_neg/total), (neut/total), (weak_pos/total), (pos/total)]

#Sets labels and titles
mplot.xlabel("Sentiment")
mplot.ylabel("Percent of Words")
mplot.title("Sentiment of Distribution for Challenge 2")

label_pos=[0.2, 1.2, 2.2, 3.2, 4.2]
bar_pos=[0.1, 1.1, 2.1, 3.1, 4.1]

mplot.bar(bar_pos, percent, color="red")
xlabels=(["negative", "weak negative","neutral", "weak positive","positive"])

mplot.xticks(label_pos, xlabels)
mplot.show()
