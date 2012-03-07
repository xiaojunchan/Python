import os
import re
import string

filelist = os.listdir(os.getcwd())
pattern = '.tif'

out = []
for file in filelist:
	if re.search(pattern, file):
		out.append(file)
		
for file in out:
	print(file)