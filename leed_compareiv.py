#	This program use GNUplot to :
#	(1) Compare different IV curve in different list file
import os, re, string, sys, subprocess

################SUB################
def leed_readlstfile(filename):
	iv_file = []
	spotx = []
	spoty = []
	columns = []
	# 	Open files
	F = open(filename,"r")
	for rows in F:
		columns = rows.split()
		columns = [col.strip() for col in columns]
		iv_file.append(columns[0])
		spotx.append(float(columns[1]))
		spoty.append(float(columns[2]))
	F.close()
	return iv_file, spotx, spoty

def leed_draft_script(title,infile,plabel,outpath,spotx,spoty):
	script=[]
	script.append("set style line 1 lt 1 lw 1")
	script.append("set style line 2 lt 2 lw 1")
	script.append("set style line 3 lt 3 lw 1")
	script.append("set style line 4 lt 6 lw 1")
	script.append("set style line 5 lt 1 lw 3")
	script.append("set style line 6 lt 2 lw 3")
	script.append("set style line 7 lt 3 lw 3")
	script.append("set style line 8 lt 6 lw 3")
	script.append("set size square")
	script.append("set xlabel \" Energy(eV) \"")
	script.append("set ylabel \" Intensity(Arbit.) \"")
	temp = []
	for file in infile:
		temp.append(file[1])
	script.append("set title \"%s\\n[%s,%s]\\n%s\"" % (title,str(spotx),str(spoty),','.join(temp)))
	#script.append("unset key")
	script.append("set terminal postscript enhanced")
	script.append("set output \"%s%s-(%s,%s).eps\"" % (outpath.replace ('\\','/'),title,str(spotx),str(spoty)))
	#	Plot different input files in the same graph
	command = ""
	plot1=[]
	for i,file in enumerate(infile):
		input = os.path.join(file[0],file[1]).replace ('\\','/')
		command = "\"%s\" every ::2 t \"%s\" w l ls %s" % (input,plabel[i],i+1)
		plot1.append(command)
	script.append("plot "+", ".join(plot1))

	return script

def leed_writeandexec_script(script):
	F = open('temp',"w")
	for item in script:
		F.write("%s\n" % item)
	F.close()
	subprocess.call(["gnuplot.exe", 'temp'])

################MAIN################
#	Read the arguments
LSTfile = sys.argv[1:]
curr_dir = os.getcwd()
#	List storing list file details
curr_dir = []
LST_file = []
LST_dir = []
#	List storing IV plot details
iv_file = []
spotx = []
spoty = []
#	Read the list files
for LST_path in LSTfile:
	#	Path treatment
	LST_file.append(os.path.basename(LST_path))
	LST_dir.append(os.path.dirname(LST_path))
	os.chdir(LST_dir[-1])
	#	Retrieve information from list file
	temp1, temp2, temp3 = leed_readlstfile(LST_file[-1])
	iv_file.append(temp1)
	spotx.append(temp2)
	spoty.append(temp3)

#	Enter the title and label for each data file
title = raw_input('Title? ').strip()
plot_label = []
for i in range(len(LSTfile)):
	plot_label.append(raw_input('Label %s? ' % str(i+1)).strip())

#	Combine all 2D lists in 1D lists
LABEL = []
for i,item in enumerate(plot_label):
	temp = [item,] * len(iv_file[i])
	LABEL = LABEL + temp
DIR = []
for i,item in enumerate(LST_dir):
	temp = [item,] * len(iv_file[i])
	DIR = DIR + temp
IVFILE = [ item for innerlist in iv_file for item in innerlist ]
SPOT_X = [ item for innerlist in spotx for item in innerlist ]
SPOT_Y = [ item for innerlist in spoty for item in innerlist ]
max_index = len(SPOT_Y)

#	Bundle the lists and sort the x index and y index
z_list = zip(SPOT_X,SPOT_Y,DIR,IVFILE,LABEL)
s_list = sorted(z_list)

#	Check difference in adjacent elements
check = [(abs(float(s_list[x][1]) - float(s_list[x+1][1])) > 0.01) for x in range(0, max_index-1)]
#	Treat true element as boundary to group corresponding file to unique spot
unique_spot = []
unique_file = []
unique_label = []
temp1 = []
temp2 = []
for i,item in enumerate(check):
	temp1.append([s_list[i][2],s_list[i][3]])
	temp2.append(s_list[i][4])
	if item:
		unique_spot.append((s_list[i][0],s_list[i][1]))
		unique_file.append(temp1)
		unique_label.append(temp2)
		temp1 = []
		temp2 = []
		
#	Search and find the same spot content
outpath = "D:\\Temp\\"
for i, spot in enumerate(unique_spot):
	x_index = spot[0]
	y_index = spot[1]
	infile = unique_file[i]
	plabel = unique_label[i]

	print ("Loading (%s,%s) index files ..." % (x_index,y_index))
	for item in infile:
		print '\\'.join(item)
	script = leed_draft_script(title,infile,plabel,outpath,x_index,y_index)
	print ("Plotting... ")
	leed_writeandexec_script(script)

subprocess.call(["rm", 'temp'])
print ("Program ended successfully... ")