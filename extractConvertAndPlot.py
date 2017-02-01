import ast
import math,sys
import matplotlib.pyplot as matplot 

_Radius = 6371

fileName = 'trainSubsetNoHeaders.csv'

f = open(fileName, 'r')

cartList = []
i=0
temp = 0;
for line in f:
	splitLine = line.split('",')
	i+=1
	percent = int(i/30)
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
		xcoord = _Radius*math.cos(coord[0]*math.pi/360)*math.cos(coord[1]*math.pi/360)
		ycoord = _Radius*math.cos(coord[0]*math.pi/360)*math.sin(coord[1]*math.pi/360)
		matplot.scatter(xcoord, ycoord)


matplot.xlabel("X-axis (km)")
matplot.ylabel("Y-axis (km)")
matplot.show()	
f.close()
