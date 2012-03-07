import os
import string
import shutil

#	Get the root Directory
top_dir = os.getcwd()
curr_dir = top_dir

def search_dat(filelist):
	pattern = '.dat'
	out = []
	for file in filelist:
		if os.path.splitext(file)[1] ==  pattern:
			out.append(file)
	return out

def get_dat_location():
	out = []
	curr_dir = ''
	curr_file = ''	
	directory_list = os.walk(mother_dir)
	for i in directory_list:
		searched_list = search_dat(i[-1])
		if len(searched_list) > 0 :
			curr_dir = i[0]
			curr_file = ''.join(searched_list)
			out.append([os.path.basename(curr_dir),curr_file])
	return out

dat_list = get_dat_location()
out_dir = mother_dir+os.sep+'out'
os.makedirs(out_dir)

for file in dat_list:
	new_dir = out_dir+os.sep+file[0]
	os.makedirs(new_dir)
	new_file_dir = os.path.join(new_dir,file[1])
	old_file_dir = os.path.join(mother_dir,file[0],file[1])
	print "copying %s to %s" % (old_file_dir,new_file_dir)
	shutil.copy2(old_file_dir,new_file_dir)

raw_input()