import sys
import ast
import math, numpy
import matplotlib.pyplot as matplot
from pylab import plot,show 
from scipy.cluster.vq import kmeans, vq, whiten

_Radius = 6371

fileName = 'trainSubsetNoHeaders.csv'
#For calculating progress percentage please specify lineCount of the file:'fileName'
lineCount = 50000

f = open(fileName, 'r')

i=0
j=0
temp = -1
cartList = []
print "\033[95m Welcome!\n \033[94m Parsing CSV input stream"

for line in f:
	splitLine = line.split('",')
	j+=1
	percent = int(j*100/lineCount)
	if percent>temp:
		temp = percent
		sys.stdout.write("\r%d%%" % percent)
		sys.stdout.flush()
	
	listOfCoords = ast.literal_eval(splitLine[8])

	if len(listOfCoords)>2:
		strs = listOfCoords.replace('[','').split('],')

		try:		
			lists = [map(float, s.replace(']','').split(',')) for s in strs]

		except ValueError, Err:
			print "\n"	
			print "Error"
			print e	
			print "__splitline[8]__"
			print splitLine[8]
			print "List of coords:"
			print listOfCoords
			print len(listOfCoords)
			print type(listOfCoords)
			break
	
	for coord in lists:
		l = []
		xcoord = _Radius*math.cos(coord[0]*math.pi/360)*math.cos(coord[1]*math.pi/360)
		ycoord = _Radius*math.cos(coord[0]*math.pi/360)*math.sin(coord[1]*math.pi/360)
		l.append(xcoord)
		l.append(ycoord)
		cartList.append(l)

f.close()

#K-Means Clustering starts here
#Caution : 
#1. The data is not whitened as the spread of overall data is not too high 
#2. Update 'color' vector with more colors when specifying _ClusterNo more than 10

_ClusterNo = 10
color = ['r','g','b','y','#009688','#673AB7', '#FF5722','k','#BCBBC1','#82B53F']
clusterGroup = []

for i in range(_ClusterNo):
	emptyList = []	
	clusterGroup.append(emptyList)

print "\n \033[94m kmeans starting now\n"

whiteData = whiten(cartList)
centroids = kmeans(numpy.array(cartList), _ClusterNo)

centroidArray = numpy.array(centroids[0])
dataArray = numpy.array(cartList)

print "\033[94m Mapping in progress\n"

mapped = vq(dataArray,centroidArray)

print "\033[94m Grouping data with reference to code and code_book\n"
l=0
for coord in cartList:
	
	for n in range(_ClusterNo):
		if mapped[0][l] == n:
			clusterGroup[n].append(coord)
			break 	
	l += 1

print "\033[94m Sacttering data\n"
k=0
for centroid in centroids[0]:
	cluster = numpy.array(clusterGroup[k])
	matplot.scatter(cluster[:,0], cluster[:,1], c=color[k])	
	matplot.scatter(centroid[0], centroid[1], s=200, c='m')
	k+=1

matplot.xlabel("X-axis (km)")
matplot.ylabel("Y-axis (km)")
print "\033[92m Success : Showing Map figure\n"
matplot.show()

