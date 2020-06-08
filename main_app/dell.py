from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dell(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(439, 205)
        Dialog.setStyleSheet("QDialog{\n"
"background-color:#34495e;\n"
"}\n"
"")
        self.dell = QtWidgets.QPushButton(Dialog)
        self.dell.setGeometry(QtCore.QRect(250, 70, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dell.setFont(font)
        self.dell.setStyleSheet("QPushButton{\n"
"background-color:none;\n"
"border-style:solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: #2ecc71;\n"
"color:white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#2ecc71;\n"
"}")
        self.dell.setObjectName("dell")
        self.slovo = QtWidgets.QLineEdit(Dialog)
        self.slovo.setGeometry(QtCore.QRect(60, 70, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.slovo.setFont(font)
        self.slovo.setStyleSheet("QLineEdit{\n"
"background-color:none;\n"
"border-style:solid;\n"
"border-width: 3px;\n"
"border-radius: 10px;\n"
"border-color: #3498db;\n"
"color:black;\n"
"}\n"
"")
        self.slovo.setObjectName("slovo")
        self.slovo_l = QtWidgets.QLabel(Dialog)
        self.slovo_l.setGeometry(QtCore.QRect(70, 20, 141, 31))
        self.slovo_l.setObjectName("slovo_l")
        self.status = QtWidgets.QLabel(Dialog)
        self.status.setGeometry(QtCore.QRect(250, 160, 141, 31))
        self.status.setStyleSheet("QLabel{color:white;}")
        font.setPointSize(12)
        self.status.setFont(font)
        self.status.setObjectName("status")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ramz_ild"))
        self.dell.setText(_translate("Dialog", "Удалить"))
        self.slovo_l.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Введите слово</span></p></body></html>"))
        self.status.setText(_translate("Dialog", ""))


