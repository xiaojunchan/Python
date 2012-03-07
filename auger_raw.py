#	Thiss program read some AES data and manipulate the data 
import os
import sys
#import auger_peckdetect

def auger_readfile(filename):
	header_list = []
	ilist = []
	# 	Open files
	f = open(filename,"r")
	for i, line in enumerate(f):
		#	Read Header Lines into list
		if i == 0:
			header_list.append(line)
		elif i == 1:
			header_list.append([])
			for j in line.split():
				header_list[-1].append(float(j))
		elif i == 2:
			header_list.append(line)
		#	Read Data Points into list
		elif i > 2:
			ilist.append(float(line))
	f.close()
	return header_list, ilist

def auger_writefile(filename,x,y,header):
	f = open(filename +".plot","w")
	#	Write headers
	for item in header:
		f.write("#\t%s" % item)
	#	Write x,y data
	for i, item in enumerate(x):
		f.write(str(item) + "\t" + str(y[i]) + "\n")
	f.close()

def normalize(x):
	x_mean = sum(x) / len(x)
	x_out = []
	for item in x:
		x_out.append(item/x_mean)
	return x_out
	
def area_under_graph(x,y):
	xiplus1 = x[1:-1]
	xi = x[0:-2]
	dA = []
	for i,item in enumerate(xi):
		dA.append((xiplus1[i] - item)*y[i])
	return sum(dA)

def area_trapezium(x1,y1,x2,y2):
	return (y1+y2)*(x2-x1)/2
	
#	Main(Check)
if __name__=="__main__":
	
	if len(sys.argv) < 2:
		print 'No action specified.'
		sys.exit()
		
	#	Main 
	for filename in sys.argv[1:]:
		#	Read from files
		header_list,y = auger_readfile(filename)
		print header_list
		#	Create x data
		x = range(len(y))
		x_min = float(header_list[1][0])
		x_step = float(header_list[1][2])
		x = map(lambda i:i*x_step+x_min, range(len(y)))
		#	output into files
		peakrange = []
		
		auger_writefile(filename,x,y,header_list)
		print area_under_graph(x,y)
	

	
