#	This program use ghostscript to :
#	(1) convert all existing EPS files in a folder to a single PDF file (by default)
#	(2) convert listed EPS files in a folder to a PDF file (If argument with eps extension exists)
#	(3) convert all existing EPS files in a path specified (If argument is a path)
import os
import re
import string
import sys
import subprocess

#	Get the current path
mother_dir = os.getcwd()
curr_dir = mother_dir

#	Read the arguments
EPSfile = sys.argv[1:]
print EPSfile
if EPSfile:
	for file in EPSfile:
		input_file = file
		output_file = file.replace('.eps','.pdf')
		print("convert %s to %s" %(input_file, output_file))
		#command = 'gswin32c.exe -sDEVICE=pdfwrite -dEmbedAllFonts=false -dOptimize=true -o %s %s' % (output_file, input_file)
		subprocess.call(["ps2pdf", input_file, output_file])

if not EPSfile:
	#	Read the files in the current directory
	filelist = os.listdir(curr_dir)
	pattern = '.eps'
	for file in filelist:
		if re.search(pattern, file):
			EPSfile.append(file)
	input_file = ' '.join(EPSfile)
	output_file = 'Binder1.pdf'
	print("convert %s to %s" %(input_file, output_file))
	subprocess.call(['gswin32c.exe','-sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dSAFER', ['-sOutputFile=',output_file], input_file])
		


