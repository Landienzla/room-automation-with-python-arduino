# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rgb.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pyfirmata import Arduino
import pyfirmata
import time
import serial.tools.list_ports


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(980, 450)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("cat pp.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setAutoFillBackground(True)
        Form.setStyleSheet("")
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 160, 82))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.scanportsbuton = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kristen ITC")
        self.scanportsbuton.setFont(font)
        self.scanportsbuton.setObjectName("scanportsbuton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.scanportsbuton)
        self.portlistbox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.portlistbox.setObjectName("portlistbox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.portlistbox)
        self.connectportbuton = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kristen ITC")
        self.connectportbuton.setFont(font)
        self.connectportbuton.setObjectName("connectportbuton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.connectportbuton)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(190, 10, 611, 191))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.redbuton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.redbuton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Kristen ITC")
        self.redbuton.setFont(font)
        self.redbuton.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.redbuton.setCheckable(False)
        self.redbuton.setObjectName("redbuton")
        self.gridLayout.addWidget(self.redbuton, 0, 0, 1, 1)
        self.bluespin = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.bluespin.setMaximum(255)
        self.bluespin.setObjectName("bluespin")
        self.gridLayout.addWidget(self.bluespin, 2, 2, 1, 1)
        self.greenbuton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kristen ITC")
        self.greenbuton.setFont(font)
        self.greenbuton.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.greenbuton.setObjectName("greenbuton")
        self.gridLayout.addWidget(self.greenbuton, 1, 0, 1, 1)
        self.Red = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.Red.setMaximum(255)
        self.Red.setOrientation(QtCore.Qt.Horizontal)
        self.Red.setObjectName("Red")
        self.gridLayout.addWidget(self.Red, 0, 1, 1, 1)
        self.Green = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.Green.setMaximum(255)
        self.Green.setOrientation(QtCore.Qt.Horizontal)
        self.Green.setObjectName("Green")
        self.gridLayout.addWidget(self.Green, 1, 1, 1, 1)
        self.bluebuton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kristen ITC")
        self.bluebuton.setFont(font)
        self.bluebuton.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.bluebuton.setObjectName("bluebuton")
        self.gridLayout.addWidget(self.bluebuton, 2, 0, 1, 1)
        self.Blue = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.Blue.setMaximum(255)
        self.Blue.setOrientation(QtCore.Qt.Horizontal)
        self.Blue.setObjectName("Blue")
        self.gridLayout.addWidget(self.Blue, 2, 1, 1, 1)

        self.r??leacbuton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kristen ITC")
        self.r??leacbuton.setFont(font)
        self.r??leacbuton.setStyleSheet("background-color: rgb(153, 192, 255);")
        self.r??leacbuton.setObjectName("r??leacbuton")

        self.r??lekapatbuton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kristen ITC")
        self.r??lekapatbuton.setFont(font)
        self.r??lekapatbuton.setStyleSheet("background-color: rgb(153, 192, 255);")
        self.r??lekapatbuton.setObjectName("r??lekapatbuton")
        self.r??lekapatbuton.move(110,0)


        self.greenspin = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.greenspin.setMaximum(255)
        self.greenspin.setObjectName("greenspin")
        self.gridLayout.addWidget(self.greenspin, 1, 2, 1, 1)
        self.redspin = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.redspin.setMaximum(255)
        self.redspin.setObjectName("redspin")
        self.gridLayout.addWidget(self.redspin, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(810, 10, 131, 189))
        self.widget.setAutoFillBackground(True)
        self.widget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.widget.setObjectName("widget")

        self.retranslateUi(Form)
        self.Red.sliderMoved['int'].connect(self.redspin.setValue)
        self.Green.sliderMoved['int'].connect(self.greenspin.setValue)
        self.Blue.sliderMoved['int'].connect(self.bluespin.setValue)
        self.redspin.valueChanged['int'].connect(self.Red.setValue)
        self.greenspin.valueChanged['int'].connect(self.Green.setValue)
        self.bluespin.valueChanged['int'].connect(self.Blue.setValue)
        QtCore.QMetaObject.connectSlotsByName(Form)
        

        self.scanportsbuton.clicked.connect(self.scanports)
        self.connectportbuton.clicked.connect(self.connectArduino)


        self.Red.valueChanged.connect(self.colorchange)
        self.Green.valueChanged.connect(self.colorchange)
        self.Blue.valueChanged.connect(self.colorchange)

        self.r??leacbuton.clicked.connect(self.lambaac)
        self.r??lekapatbuton.clicked.connect(self.lambakapat)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Landienzla"))
        self.scanportsbuton.setText(_translate("Form", "Scan Ports"))
        self.connectportbuton.setText(_translate("Form", "Connect"))
        self.redbuton.setText(_translate("Form", "RED"))
        self.greenbuton.setText(_translate("Form", "GREEN"))
        self.bluebuton.setText(_translate("Form", "BLUE"))
        self.r??leacbuton.setText(_translate("Form","Open Lights"))
        self.r??lekapatbuton.setText(_translate("Form","Close Lights"))
    def scanports(self):
        self.portlistbox.clear()
        ports = serial.tools.list_ports.comports()
        portlist= list()
        for p in ports:
            print(p.device)
            print(len(ports), 'ports found')
            if len(ports) > 1:
                portlist.append(p.device)
        
        self.portlistbox.addItems(portlist)
    def connectArduino(self):
        selectedport = str(self.portlistbox.currentText())
        global board
        global redledpin
        global blueledpin
        global greenledpin
        global lamba
        
        lamba = False
        board = Arduino(str(selectedport))
        redledpin = board.get_pin('d:5:p')
        greenledpin = board.get_pin('d:6:p')
        blueledpin= board.get_pin('d:3:p')

        board.digital[5].write(1)
        board.digital[6].write(0)
        board.digital[2].write(1)


    def colorchange(self):
        redvalue = int(self.Red.value())
        greenvalue = int(self.Green.value())
        bluevalue = int(self.Blue.value())
        redledpin.write(redvalue)
        greenledpin.write(greenvalue)
        blueledpin.write(bluevalue)
        board.digital[13].write(1)
        time.sleep(0.1)
        board.digital[13].write(0)
        time.sleep(0.1)
        board.digital[13].write(1)

    def lambaac(self):
        board.digital[2].write(0)
    def lambakapat(self):
        board.digital[2].write(1)

        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
