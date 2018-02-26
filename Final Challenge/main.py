"""

Hailey Cray-Dubaz
YellowButterfly
10/5/17
Final Challenge
"""
from __future__ import division
import csv 
import neuro
import linear_algebra
import numpy as np

inputs = []
targets = []
reps = 1300
network = []

data = open('test_cases.csv')
data = data.read()
data = data.split('\n')
data.pop()

for i in data:
	tokens = i.split(',')
	inputs.append([float(tokens[0]), float(tokens[1]), float(tokens[2])])
	targets.append([float(tokens[3])])

	
network = neuro.setup_network(inputs)
neuro.train(network,inputs,targets,reps)

user_answer = 'y'
while user_answer == 'y':

	r = float(raw_input("Enter a value for red between 0 and 255: "))/255
	g = float(raw_input("Enter a value for green between 0 and 255: "))/255
	b = float(raw_input("Enter a value for blue between 0 and 255: "))/255
	pred = round(neuro.predict(network,[r,g,b]), 2)


	if (pred >= 0.0 and pred < 0.33):
			print("\nThe color is RED!\n")
	elif (pred >= 0.33 and pred < 0.66):
			print("\nThe color is GREEN!\n")
	elif (pred >= 0.66 and pred < 1.0):
			print("\nThe color is BLUE!\n")

	user_answer=raw_input("Again? (y/n): ")