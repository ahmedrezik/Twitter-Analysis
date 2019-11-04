import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
file = pd.read_csv("saraAlaa.csv")

time = file['created_at']
tim = []
for i in range(len(time)):
	tim.append(time[i].split(' '))

fintim = []
for i in range(len(tim)):
	fintim.append(tim[i][1][0])
	fintim[i] += tim[i][1][1]
	fintim[i] = int(fintim[i])




xAxis = []
for i in range(25):
	xAxis.append(i)


def occ(arr,n):
	count = 0 
	for i in range(len(arr)):
		if(arr[i] == n and arr[i] != -1):
			count+= 1
			arr[i] = -1
			
			
	
	return n,count


def arrcount(arr):
	fin = []
	for i in range(len(arr)):
		fin.append(occ(arr,arr[i]))
	return fin



tup = arrcount(fintim)


out_tup = [i for i in tup if i[0] >= 0]
		
x = []
y =[]

for i in range(len(out_tup)):
	x.append(out_tup[i][0])
	y.append(out_tup[i][1])










plt.bar(x,y, 0.5, color="red")
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.title('Sara Twitter Activity')
plt.ylabel("Number of tweets posted")
plt.xlabel("Time in 24 hrs format")
plt.show()