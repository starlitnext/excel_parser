#-*- coding:utf-8 -*-


class ExcelCell(object):

	def __init__(self):
		pass


class ExcelHead(object):

	def __init__(self, cells=[]):
		self.cells = cells

	def append(self, cell):
		self.cells.append(cell)

	def insert(self, idx, cell):
		self.cells.insert(idx, cell)

	def removeByIndex(self, idx):
		self.cells.pop(idx)

	def removeByName(self, cell):
		try:
			while 1:
				self.cells.remove(cell)
		except ValueError:
			return

	def extend(self, cells):
		self.cells.extend(cells)

	def __repr__(self):
		return '<ExcelHead>: ' + str(self.names)

	def __str__(self):
		return str(self.names)



class ExcelRowData(object):

	def __init__(self):
		pass


class ExcelSheet(object):

	def __init__(self):
		self.head = None
		self.data = None

	pass