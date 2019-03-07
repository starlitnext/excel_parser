#-*- coding:utf-8 -*-
# 写入格式参考 https://blog.csdn.net/onlyanyz/article/details/45348279

import xlwt


class ExcelWriter(object):

	def __init__(self, filename):
		self.filename = filename


def set_stype(name, height, bold=False):
	style = xlwt.XFStyle()
	font = xlwt.Font()
	font.name = name
	font.bold = bold
	font.colour_index = 4
	font.height = height
	style.font = font
	return style


if __name__ == '__main__':
	wb = xlwt.Workbook('utf-8')

	# add Sheet
	sheet1 = wb.add_sheet('Sheet1', cell_overwrite_ok=True)
	# rows and cols
	row0 = ['姓名', '年龄', '出生日期', '爱好']
	colum0 = ['张三', '李四', '练习python', '小明', '小红', '无名']
	# first row
	for i in range(0, len(row0)):
		sheet1.write(0, i, row0[i], set_stype('Times New Roman', 220, True))
	# first col
	for i in range(0, len(colum0)):
		sheet1.write(i+1, 0, colum0[i], set_stype('Times New Roman', 220, True))
	sheet1.write(1, 3, '2006/12/12')
	sheet1.write_merge(6, 6, 1, 3, '未知')  # 合并行单元格
	sheet1.write_merge(1, 2, 3, 3, '打游戏')  # 合并列单元格
	sheet1.write_merge(4, 5, 3, 3, '打篮球')

	wb.save('out.xls')

	pass