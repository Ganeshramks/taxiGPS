import ast
import math, numpy
import matplotlib.pyplot as matplot
from pylab import plot,show 
from scipy.cluster.vq import kmeans, vq, whiten

_Radius = 6371000

f = open('trainData.csv', 'r')
i=0
color = 'b'
cartList = []
for line in f:
	splitLine = line.split('",')
	listOfCoords = ast.literal_eval(splitLine[8])
	strs = listOfCoords.replace('[','').split('],')
	lists = [map(float, s.replace(']','').split(',')) for s in strs]	
	for coord in lists:
		l = []
		xcoord = _Radius*math.cos(coord[0]*math.pi/360)*math.cos(coord[1]*math.pi/360)
		ycoord = _Radius*math.cos(coord[0]*math.pi/360)*math.sin(coord[1]*math.pi/360)
		l.append(xcoord)
		l.append(ycoord)
		cartList.append(l)

f.close()

#K-Means Clustering starts here
#caution : the data is not whitened as the spread of the overall data is not too high 

whiteData = whiten(cartList)
centroids = kmeans(numpy.array(cartList), 5)
#centroids = kmeans(whiteData, 5)
centroidArray = numpy.array(centroids[0])
dataArray = numpy.array(cartList)

mapped = vq(dataArray,centroidArray)

for coord in cartList:
	if (mapped[0][i] == 0):
		color = 'b'
	elif (mapped[0][i] == 1):
		color = 'r'
	elif (mapped[0][i] == 2):
		color = 'g'
	elif (mapped[0][i] == 3):
		color = 'y'
	else:
		color = 'k'
	i += 1
	matplot.scatter(coord[0], coord[1], c=color)

for centroid in centroids[0]:
	matplot.scatter(centroid[0], centroid[1], s=100, c='m')

matplot.xlabel("X-axis (m)")
matplot.ylabel("Y-axis (m)")
matplot.show()




