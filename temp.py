import sys, os, csv
import Gnuplot

def search_spot(x_required,y_required,file_list):
	if x_required == file_list.get(x[i]):
		if y_required == file_list.get(y[i]):
			return file_list.get(file[i])
	else: return NULL

str_path = '..\\..\\..\\..\\LEED\\SnO2(110)\\Result\\20110902b\\NORM\\nomirror\\'
str_listfile = 'norm.lis'
os.chdir(str_path)

#	Read file
order = ['file','x','y']
file_list = {}  
file_list = csv.DictReader(open(str_listfile, 'rb'),  order, delimiter='\t')
for row in file_list:
    

print "Please enter the index (x,y):1"
x_required = raw_input('x:\t')
y_required = raw_input('y:\t')
	
search_spot(x_required,y_required,file_list)



