import ast
import math
import matplotlib.pyplot as matplot 

_Radius = 6371000

f = open('trainData.csv', 'r')
i=0
cartList = []
for line in f:
	splitLine = line.split('",')
	listOfCoords = ast.literal_eval(splitLine[8])
	strs = listOfCoords.replace('[','').split('],')
	lists = [map(float, s.replace(']','').split(',')) for s in strs]	
	#print lists
	#print type(lists)
	for coord in lists:
		l = []
		xcoord = _Radius*math.cos(coord[0]*math.pi/360)*math.cos(coord[1]*math.pi/360)
		ycoord = _Radius*math.cos(coord[0]*math.pi/360)*math.sin(coord[1]*math.pi/360)
		l.append(xcoord)
		l.append(ycoord)
		cartList.append(l)
		matplot.scatter(xcoord, ycoord)

		#print "coordinates"
print cartList
matplot.show()	
f.close()
