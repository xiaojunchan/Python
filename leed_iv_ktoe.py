#	This program use GNUplot to :
#	(1) Plot all the IV curve in the directory
import os
import re
import string
import sys
import subprocess

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

def leed_draft_script(title,infile,outfile,spotx,spoty):
	script=[]
	script.append("set size square")
	script.append("set xlabel \" Energy(eV) \"")
	script.append("set ylabel \" Intensity(Arbit.) \"")
	script.append("set title \"%s\\n(%s,%s)\\n%s\"" % (title,str(spotx),str(spoty),infile))
	script.append("unset key")
	script.append("set terminal postscript enhanced")
	script.append("set output \"%s-(%s,%s).eps\"" % (title,str(spotx),str(spoty)))
	script.append("plot \"%s\" with lines" % infile)
	return script

def leed_writeandexec_script(script):
	F = open('temp',"w")
	for item in script:
		F.write("%s\n" % item)
	F.close()
	subprocess.call(["gnuplot.exe", 'temp'])
	

################MAIN################
title = "SnO2"
#	Read the arguments
LSTfile = sys.argv[1]
#	Path treatment
curr_dir = os.getcwd()
LST_path = LSTfile
LST_file = os.path.basename(LST_path)
LST_dir = os.path.dirname(LST_path)
os.chdir(LST_dir)

#	Plot all the IV curve
iv_file, spotx, spoty = leed_readlstfile(LST_file)
for i,file in enumerate(iv_file):
	infile = file
	outfile = infile.replace('.h','.eps')
	print ("Loading... \t %s" % infile)
	script = leed_draft_script(title,infile,outfile,spotx[i],spoty[i])
	print ("Plotting...  \t %s" % outfile)
	leed_writeandexec_script(script)

remove('temp')