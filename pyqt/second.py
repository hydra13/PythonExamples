# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
import sys

class CounterWidget(QtWidgets.QWidget):
	lDigit = 0
	pbPlus = 0
	pbMinus = 0
	pbExit = 0
	vBox = 0
	def __init__(self):
		super(CounterWidget, self).__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle("Counter")
		self.resize(300, 400)

		self.lDigit = QtWidgets.QLabel("0")
		font = self.lDigit.font()
		font.setPixelSize(40)
		self.lDigit.setFont(font)
		self.lDigit.setAlignment(QtCore.Qt.AlignCenter)

		font.setPixelSize(16)
		font.setBold(True)
		self.pbPlus = QtWidgets.QPushButton("+")
		self.pbMinus = QtWidgets.QPushButton("-")
		self.pbExit = QtWidgets.QPushButton("Exit")
		self.pbPlus.setFont(font)
		self.pbMinus.setFont(font)
		self.pbExit.setFont(font)

		self.pbPlus.clicked.connect(self.onPlusClicked)
		self.pbMinus.clicked.connect(self.onMinusClicked)
		self.pbExit.clicked.connect(QtWidgets.qApp.quit)

		self.vBox = QtWidgets.QVBoxLayout()
		self.vBox.addWidget(self.pbPlus)
		self.vBox.addWidget(self.lDigit)
		self.vBox.addWidget(self.pbMinus)
		self.vBox.addWidget(self.pbExit)
		self.setLayout(self.vBox)

	def onPlusClicked(self):
		x = int(self.lDigit.text())
		x += 1
		self.lDigit.setText(str(x))

	def onMinusClicked(self):
		x = int(self.lDigit.text())
		x -= 1
		self.lDigit.setText(str(x))



def Main():
	# Create main widget
	app = QtWidgets.QApplication(sys.argv)
	window = CounterWidget()
	window.show()
	sys.exit(app.exec_())


if __name__ == "__main__":
	Main()