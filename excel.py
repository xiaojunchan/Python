#!/usr/bin/env python
import win32com.client
#	Main
#	Connect with Excel Current workbook and worksheet
##	SubRoutine
#	Read the specific range

obj = win32com.client.Dispatch("Excel.Application")
obj.Visible = 1
currentbook = obj.ActiveWorkbook
currentsheet = currentbook.ActiveSheet
s = currentsheet
max_row = currentsheet.usedrange.rows.count 
max_col = currentsheet.usedrange.columns.count

def xRange(s_row,e_row,s_col,e_col):
	data = s.Range(s.Cells(s_row,s_col), s.Cells(e_row,e_col)).Value
	return data
	
#	Read the specific column
def xCol(col):
	col_list = []
	for i in range(1,max_row + 1):
		col_list.append(s.Cells(i,col).Value)
	return col_list

#	Read the specific column
def xRow(row):
	col_list = []
	for i in range(1,max_col + 1):
		col_list.append(s.Cells(row,i).Value)
	return col_list
	
#	Read the specific cell
def xCell(row,col):
	return s.Cells(row,col).Value

def Select_xCell(row,col):
	s.Cells(row,col).Select()
	s.Cells(row,col).Activate()
	
def write_xCell(row,column,value,type):
	if type == 'I':
		s.Cells(int(row),column).Value = int(round(float(value)))
	if type == 'F':
		s.Cells(int(row),column).Value = float(value)
	if type == 'S':
		s.Cells(int(row),column).Value = str(value)
		
def write_xRow(row,list):
	for i in range(1,max_col + 1):
		s.Cells(row,i).Value = list[i]
		
def write_xCol(col,list):
	for i in range(1,max_row + 1):
		s.Cells(i,col).Value = list[i]

#	Convert a list to contains integer only
def ToInt(list):
	temp_list = []
	for item in list:
		if item is None:
			temp_list.append(0)
		else:
			try:
				temp_list.append(int(round(float(item))))
			except:
				temp_list.append(0)
	return temp_list

#	Convert a list to contains float only
def ToFloat(list):
	temp_list = []
	for item in list:
		if item is None:
			temp_list.append(0.0)
		else:
			try:
				temp_list.append(float(item))
			except:
				temp_list.append(0.0)
	return temp_list

#	Convert a list to contains string only
def ToStr(list):
	temp_list = []
	for item in list:
		if item is None:
			temp_list.append('')
		else:
			try:
				temp_list.append(str(item))
			except:
				temp_list.append('')
	return temp_list

##	End Of SubRoutine
def SearchString(list,search_string):
	result_list = []
	for i,item in enumerate(list):
		if search_string in item:
			result_list.append(i)
	return result_list

if __name__ == "__main__":
	import win32com.client
	obj = win32com.client.Dispatch("Excel.Application")
	obj.Visible = 1
	currentbook = obj.ActiveWorkbook
	currentsheet = currentbook.ActiveSheet
	s = currentsheet
	max_row = currentsheet.usedrange.rows.count 
	max_col = currentsheet.usedrange.columns.count