#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 11:18:50 2017

@author: Hailey Cray-Dubaz
Spirit Animal User ID: Yellow Butterfly
Date Last Edited: 10/6/17
Challenge #3

Tutor for Python: Will Sanefski
Code taken from Lecture 10 and Class Wiki
"""
import matplotlib.pyplot as mplot
from PIL import Image
import numpy as np
import os

images = os.listdir("unionconstruction")

img_list=[]

threshold = int(input("Enter your change threshold (values only between 0 and 255 are accepted): "))   
    
for i in range(0, len(images)):
    if ".jpg" in images[i]:
        img =np.float32(Image.open("unionconstruction/" + images[i]))
        img_list.append(img)

   
avg_img=[]
for img in img_list:
    try:
        avg_img = avg_img + img
    except:
        avg_img = img

avg_img /= len( img_list )


std_img = [0,0,0]
for img in range(len(img_list)):
        std_img += (img_list[img] - avg_img)**2
        
std_img /= len( images )
std_img = np.sqrt(std_img)

      
for row in range(len(std_img)): #loops over the number of rows in the image
    for col in range(len(std_img[row])): # loops over the number of columns in the current row
        if(sum(std_img[row][col])/3 > threshold):   
            avg_img[row][col]=[255.0, 0.0, 0.0]
    
    
avg_img=np.clip(avg_img, 0, 255)
avg_img=np.uint8(avg_img)
mplot.imshow(avg_img)
mplot.show()
