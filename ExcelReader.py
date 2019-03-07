#-*- coding:utf-8 -*-

import xlrd


class ExcelReader(object):

	def __init__(self):
		pass


if __name__ == '__main__':
	# open a Excel file
	data = xlrd.open_workbook("Excel1.xls")
	print (data.sheet_names())
	# open the first sheet
	# table = data.sheets()[0]
	# table = data.sheet_by_name('Sheet1')
	table = data.sheet_by_index(0)
	# get the rows of the first sheet
	print 'rows of the first sheet:', table, table.nrows, table.ncols
	# get row/col values
	# print table.row_values(2)
	# print table.col_values(2)
	for i in range(table.nrows):
		print table.row_values(i)

	cell_A1 = table.cell(0, 0).value.encode('utf-8')
	print cell_A1, table.cell(1, 1)
	cell_B1 = table.row(0)[1].value.encode('utf-8')
	print cell_B1
	pass