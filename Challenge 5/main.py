'''
@author: Hailey Cray-Dubaz
Spirit Animal User ID: Yellow Butterfly
Date Last Edited: 11/1/17
Challenge #5

Some code was taken from lecture slides (Lecture 2)
Some code was taken from wiki (Polynomial Regression)
'''

from __future__ import division
import matplotlib.pyplot as mplot
import numpy as np

file=open("YellowButterfly_ch5.csv", "r") 
data=file.read()
data=data.strip()
data=data.split('\n')

xCoordinates=[]
yCoordinates=[]

for line in data:
   
   line=line.split(",") 
   line[0]=float(line[0])
   line[1]=float(line[1])
   line[2] =float(line[2])
   if line[2] == 26.384451:
       xCoordinates.append(line[0])
       yCoordinates.append(line[1])
       
degree = int(raw_input("Please input the degree you wish to test: "))

model_params=np.polyfit(xCoordinates, yCoordinates, degree)
y_predicted = np.polyval(model_params, xCoordinates)
       
mplot.xlabel("Milliseconds")
mplot.ylabel("Amplitude")
mplot.title("Challenge 5")
mplot.scatter(xCoordinates, yCoordinates)
mplot.plot(xCoordinates, y_predicted, color='red')
mplot.show()
