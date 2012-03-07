#	Thiss program read some AES data and plot the graph
from os import system, remove
import sys

def Plotscript(filelist,headerposition):
	plot1 = [\
		"set terminal postscript enhanced mono \"Helvetica\" 14 ",\
		#"set multiplot",\
		"set style line 1 lt 1 lw 1",\
		"set style line 2 lt 2 lw 1",\
		"set style line 3 lt 3 lw 1",\
		"set style line 4 lt 6 lw 1",\
		"set style line 5 lt 1 lw 3",\
		"set style line 6 lt 2 lw 3",\
		"set style line 7 lt 3 lw 3",\
		"set style line 8 lt 6 lw 3",\
		]
	out_file = "out.eps"
	plotcommand = "set output \"%s\"" % (out_file)
	plot1.append(plotcommand)
	plot2 = []
	plotcommand = ""
	for i,filename in enumerate(filelist):
		plotcommand = "\"%s\" every ::2 w l ls %s" % (filename,i+1)
		plot2.append(plotcommand)
	plot1.append("plot "+", ".join(plot2))
	return plot1

def Plot(slist):
	f = open("temp",'w')
	for item in slist:
		f.write("%s\n" % item)
	f.close()
	
#	Main(Check)
if len(sys.argv) < 2:
	print 'No action specified.'
	sys.exit()

#	Main
headerposition = 5
Plot(Plotscript(sys.argv[1:], headerposition))
system('gnuplot.exe temp')
#remove('temp')