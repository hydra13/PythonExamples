# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
import sys

def Main():
	# Create main widget
	app = QtWidgets.QApplication(sys.argv)
	window = QtWidgets.QWidget()
	window.setWindowTitle("Counter")
	window.resize(300, 400)

	# Create and configure label
	lDigit = QtWidgets.QLabel("0")
	font = lDigit.font()
	font.setPixelSize(40)
	lDigit.setFont(font)
	lDigit.setAlignment(QtCore.Qt.AlignCenter)

	# Create and configure buttons
	font.setPixelSize(16)
	font.setBold(True)
	pbPlus = QtWidgets.QPushButton("+")
	pbMinus = QtWidgets.QPushButton("-")
	pbExit = QtWidgets.QPushButton("Exit")
	pbPlus.setFont(font)
	pbMinus.setFont(font)
	pbExit.setFont(font)

	# Init connections
	pbPlus.clicked.connect(lambda x: onPlusClicked(lDigit))
	pbMinus.clicked.connect(lambda x: onMinusClicked(lDigit))
	pbExit.clicked.connect(app.quit)

	vBox = QtWidgets.QVBoxLayout()
	vBox.addWidget(pbPlus)
	vBox.addWidget(lDigit)
	vBox.addWidget(pbMinus)
	vBox.addWidget(pbExit)
	window.setLayout(vBox)

	window.show()
	sys.exit(app.exec_())

def onPlusClicked(lDigit):
	x = int(lDigit.text())
	x += 1
	lDigit.setText(str(x))

def onMinusClicked(lDigit):
	x = int(lDigit.text())
	x -= 1
	lDigit.setText(str(x))


if __name__ == "__main__":
	Main()