'''
@author: Hailey Cray-Dubaz
Spirit Animal User ID: Yellow Butterfly
Date Last Edited: 11/1/17
Challenge #4

Some code was taken from lecture slides
Tutored by Paul
'''
from __future__ import division
import matplotlib.pyplot as mplot
import numpy as np
import sys
import math
 
 'code from wiki'
def dist(a, b):
    return math.sqrt(math.pow(a[0]-b[0],2)+math.pow(a[1]-b[1],2))
#found on internet
def column(matrix, i):
    return [row[i] for row in matrix]

#opening data file
'code from lecture 2'
file=open("data_ch4/data.csv", "r")
data=file.read()
data=data.strip()
data=data.split('\n')

#converting file to list of floats
'code from lecture 2'
data_list=[]
for line in data:
   line=line.split(",") 
   line[0]=float(line[0])
   line[1]=float(line[1])
   line[2] =float(line[2])
   data_list.append(line)

#Inputs K value
k=int(raw_input("How many elements do you want to display (integer must be above 0):"))

#Checks whether k input is above 0
if (k > 0):
    pass
else:
    sys.exit("Integer is not above 0!")

#Calculating distance and average
'Paul gave pseudo code for this'
avg_list=[]
for row in range(192):
    for col in range(120):
        distance=[]
        for points in data_list:    
            distance.append([row,col,dist([row,col],[points[0],points[1]]), points[2]])
        distance=sorted(distance, key=lambda val:val[2])
        distance=distance[0:k]
        
        #averaging the colors
        sum=0
        for i in range(k):
            sum+=distance[i][3]
        avg=sum/k
        avg_list.append([row, col, avg])

#Empty lists fro reconstructed values
'class explanation'
recon_x=[]
recon_y=[]
recon_v=[]

#Adds reconstructed values to lists
x= column(avg_list, 0)
recon_x.append(x)

y = column(avg_list, 1)
recon_y.append(y)

v=column(avg_list, 2)
recon_v.append(v)

#Outlines the United States
'found this online'
u, s = np.loadtxt('data_ch4/us_outline.csv', delimiter=',', unpack=True)
mplot.plot(u,s, color="black")

#Scatter plotting x,y for your kNN program
#Set your color (c) to your list of reconstructed values (not sure if it means the third column)
#Set your colormap (cmape) to the "Viridis" scheme
mplot.scatter(recon_x, recon_y, c=recon_v, cmap='viridis')
mplot.show()
