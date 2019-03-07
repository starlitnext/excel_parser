#-*- coding:utf-8 -*-

import sys
from PyQt5 import QtWidgets
from FileDialog import FileOpenWidget
from ExcelFilterWidget import ExcelFilterWidget


class MainWindow(QtWidgets.QWidget):
	
	def __init__(self):
		super(MainWindow, self).__init__()

		mainLayout = QtWidgets.QHBoxLayout()

		self.fileWidget = FileOpenWidget()
		self.filterWidget = ExcelFilterWidget()

		self.filterBtn = QtWidgets.QPushButton()
		self.filterBtn.setText('开始')
		self.filterBtn.clicked.connect(self.onFilterBtnClick)

		mainLayout.addWidget(self.fileWidget)
		mainLayout.addWidget(self.filterWidget)
		mainLayout.addWidget(self.filterBtn)

		self.setLayout(mainLayout)

	def onFilterBtnClick(self):
		print '列名: ', self.filterWidget.getColName()
		print '筛选集合: ', self.filterWidget.getFilterSet()
		print '筛选条件: ', self.filterWidget.getFilterArg()
		print '筛选文件列表: ', self.fileWidget.getFiles()
		print '保存文件: ', self.fileWidget.getSaveFileName()


def main():
	app = QtWidgets.QApplication(sys.argv)
	window = MainWindow()
	window.resize(900, 400)
	window.setWindowTitle('Excel 筛选')
	window.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()