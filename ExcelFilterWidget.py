#-*- coding:utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui


class ExcelFilterWidget(QtWidgets.QWidget):
	
	def __init__(self):
		super(ExcelFilterWidget, self).__init__()

		mainLayout = QtWidgets.QVBoxLayout()

		layout = QtWidgets.QHBoxLayout()
		label = QtWidgets.QLabel('列名:    ')
		self.colNameText = QtWidgets.QLineEdit()
		layout.addWidget(label)
		layout.addWidget(self.colNameText)
		mainLayout.addLayout(layout)

		layout = QtWidgets.QHBoxLayout()
		label = QtWidgets.QLabel('筛选集合:')
		self.filterSetText = QtWidgets.QTextEdit()
		self.filterSetText.setMaximumHeight(300)
		cursor = self.filterSetText.textCursor()
		charFormat = cursor.charFormat()
		font = QtGui.QFont('Times New Roman', 10, 10, False)
		font.setBold(True)
		charFormat.setFont(font)
		cursor.setCharFormat(charFormat)
		self.filterSetText.setTextCursor(cursor)
		self.filterSetText.setTextColor(QtGui.QColor(120, 0, 0))

		layout.addWidget(label)
		layout.addWidget(self.filterSetText)
		mainLayout.addLayout(layout)

		layout = QtWidgets.QHBoxLayout()
		label = QtWidgets.QLabel('筛选条件:')
		self.filterArgText = QtWidgets.QLineEdit()
		layout.addWidget(label)
		layout.addWidget(self.filterArgText)
		mainLayout.addLayout(layout)

		# btn = QtWidgets.QPushButton('测试')
		# btn.clicked.connect(self.onTestClick)
		# mainLayout.addWidget(btn)
		self.setLayout(mainLayout)

	def getColName(self):
		return self.colNameText.text()

	def getFilterSet(self):
		ret = set()
		for text in self.filterSetText.toPlainText().splitlines():
			text and ret.add(text.encode('utf-8'))

		return ret

	def getFilterArg(self):
		return self.filterArgText.text().encode('utf-8')

	def onTestClick(self):
		print self.getColName(), self.getColName().encode('utf-8') == '你好'
		print self.getFilterSet()
		print self.getFilterArg()


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	mainWindow = ExcelFilterWidget()
	mainWindow.setWindowTitle('测试ExcelFilterWidget')
	mainWindow.show()
	sys.exit(app.exec_())
