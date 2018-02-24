from __future__ import division
import matplotlib.pyplot as mplot

file=open("YellowButterfly_ch1.csv", "r") 
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
   if line[2] == 43.574679:
		xCoordinates.append(line[0])
		yCoordinates.append(line[1])
	
data_list={}

for i in xCoordinates:
	try:
		data_list[i] += 1
	except:
		data_list[i] = 1
avgYcoordinates=[]
count=0

for key, value in data_list.items():
	sum = 0
	for term in range(value):
		sum+=yCoordinates[count]
		count += 1
	avgYcoordinates.append(sum/value)

x=[]
for key, value in data_list.items():
	x.append(key)

x=sorted(x)

mplot.xlabel("Milliseconds")
mplot.ylabel("Amplitude")
mplot.title("Challenge 1: Time vs Amplitude")
mplot.scatter(xCoordinates, yCoordinates)
mplot.plot(x, avgYcoordinates, 'r')
mplot.show()
