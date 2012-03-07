import os
import re
import string

mother_dir = os.getcwd()
curr_dir = mother_dir
filelist = os.listdir(curr_dir)
pattern = '.tif'

out = []
for file in filelist:
	if re.search(pattern, file):
		out.append(file)
		
for file in out:
	input_file = file
	output_file = file.replace('tif','jpg')
	print("convert %s to %s" %(input_file, output_file))
	command = 'convert %s -auto-level -evaluate log 100 -negate %s' % (input_file, output_file)
	os.system(command)
