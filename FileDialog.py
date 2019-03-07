#-*- coding:utf-8 -*-

import sys
import os
import copy
from PyQt5 import QtWidgets


class FileOpenWidget(QtWidgets.QWidget):

	def __init__(self):
		super(FileOpenWidget, self).__init__()
		self.cwd = os.getcwd()
		self.resize(500, 400)

		leftLayout = QtWidgets.QVBoxLayout()

		label = QtWidgets.QLabel('当前文件夹:')
		self.cwdLabel = QtWidgets.QLabel(self.cwd)
		leftTopTopLayout = QtWidgets.QHBoxLayout()
		leftTopTopLayout.addWidget(label)
		leftTopTopLayout.addWidget(self.cwdLabel)
		leftLayout.addLayout(leftTopTopLayout)

		label = QtWidgets.QLabel('保存文件:')
		self.saveFileLabel = QtWidgets.QLabel()
		leftTopTopLayout = QtWidgets.QHBoxLayout()
		leftTopTopLayout.addWidget(label)
		leftTopTopLayout.addWidget(self.saveFileLabel)
		leftLayout.addLayout(leftTopTopLayout)

		label = QtWidgets.QLabel('已选择文件列表')
		btnDel = QtWidgets.QPushButton(self)
		btnDel.setText('删除')
		btnDel.clicked.connect(self.onDelClick)
		btnClear = QtWidgets.QPushButton(self)
		btnClear.setText('清空')
		btnClear.clicked.connect(self.onClearClick)

		leftTopLayout = QtWidgets.QHBoxLayout()
		leftTopLayout.addWidget(label)
		leftTopLayout.addWidget(btnDel)
		leftTopLayout.addWidget(btnClear)

		self.choosenFilesList = QtWidgets.QListWidget(self)
		self.choosenFilesList.setMaximumHeight(300)
		self.choosenFilesList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
		self.choosenFilesList.itemDoubleClicked.connect(self.onItemDoubleClick)

		leftLayout.addLayout(leftTopLayout)
		leftLayout.addWidget(self.choosenFilesList)

		self.btnChooseDir = QtWidgets.QPushButton(self)
		self.btnChooseDir.setObjectName('btn_chooseDir')
		self.btnChooseDir.setText('选择文件夹')

		self.btnChooseMutiFile = QtWidgets.QPushButton(self)
		self.btnChooseMutiFile.setObjectName('btn_chooseMutiFile')
		self.btnChooseMutiFile.setText('选择多个文件')

		self.btnSaveFile = QtWidgets.QPushButton(self)
		self.btnSaveFile.setObjectName('btn_saveFile')
		self.btnSaveFile.setText('保存文件')

		rightLayout = QtWidgets.QHBoxLayout()
		rightLayout.addWidget(self.btnChooseDir)
		rightLayout.addWidget(self.btnChooseMutiFile)
		rightLayout.addWidget(self.btnSaveFile)

		layout = QtWidgets.QVBoxLayout()
		layout.addLayout(leftLayout)
		layout.addLayout(rightLayout)
		self.setLayout(layout)

		self.btnChooseDir.clicked.connect(self.slotBtnChooseDir)
		self.btnChooseMutiFile.clicked.connect(self.slotBtnChooseMutiFile)
		self.btnSaveFile.clicked.connect(self.slotBtnSaveFile)

		self.choosenFiles = []
		self.saveFileName = ''

	def slotBtnChooseDir(self):
		dirChoose = QtWidgets.QFileDialog.getExistingDirectory(self, '选取文件夹', self.cwd)
		if dirChoose == '':
			print '\n取消选择'
			return
		os.chdir(dirChoose)
		self.cwd = os.getcwd()
		self.cwdLabel.setText(self.cwd)

	def slotBtnChooseFile(self):
		fileNameChoose, fileType = QtWidgets.QFileDialog.getOpenFileName(self, '选取文件', self.cwd, 'All Files (*);;xls Files (*.xls)')
		if fileNameChoose == '':
			return
		print '\n你选择的文件为: ', fileNameChoose
		print '文件筛选器类型: ', fileType

	def slotBtnChooseMutiFile(self):
		files, fileType = QtWidgets.QFileDialog.getOpenFileNames(self, '选取多个文件', self.cwd, 'All Files (*);;xls Files (*.xls);;xlsx Files (*.xlsx)')
		if len(files) == 0:
			return
		for filename in files:
			if filename not in self.choosenFiles:
				self.choosenFiles.append(filename)
		self.refreshChoosenList()

	def slotBtnSaveFile(self):
		fileNameChoose, fileType = QtWidgets.QFileDialog.getSaveFileName(self, '保存文件', self.cwd, 'All Files (*);;xls Files (*.xls);;xlsx Files (*.xlsx)')
		if fileNameChoose == '':
			print '\n取消选择'
			return
		self.saveFileName = fileNameChoose
		self.saveFileLabel.setText(self.saveFileName)

	def removeFile(self, filename):
		self.choosenFiles.remove(filename)
		self.refreshChoosenList()

	def onDelClick(self):
		items = self.choosenFilesList.selectedItems()
		for item in items:
			filename = item.text()
			self.choosenFiles.remove(filename)
		self.refreshChoosenList()

	def onClearClick(self):
		self.choosenFilesList.clear()
		self.choosenFiles = []

	def onItemDoubleClick(self, item):
		self.removeFile(item.text())

	def refreshChoosenList(self):
		self.choosenFilesList.clear()
		self.choosenFiles.sort()
		for filename in self.choosenFiles:
			self.choosenFilesList.addItem(filename)

	def getFiles(self):
		return copy.deepcopy(self.choosenFiles)

	def getSaveFileName(self):
		return self.saveFileName


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	mainWindow = FileOpenWidget()
	mainWindow.setWindowTitle('测试QFileDialog')
	mainWindow.show()
	sys.exit(app.exec_())
