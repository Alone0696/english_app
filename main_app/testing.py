from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Testing(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 302)
        Dialog.setStyleSheet("QDialog{\n"
"background-color:#34495e;\n"
"\n"
"}\n"
"")
        self.digit = QtWidgets.QLabel(Dialog)
        self.digit.setGeometry(QtCore.QRect(27, 95, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.digit.setFont(font)
        self.digit.setStyleSheet("QLabel{\n"
"color:white;\n"
"}")
        self.digit.setObjectName("digit")
        self.question = QtWidgets.QLabel(Dialog)
        self.question.setGeometry(QtCore.QRect(165, 20, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.question.setFont(font)
        self.question.setObjectName("question")
        self.question.setStyleSheet("QLabel{\n"
"color:white;\n"
"}")
        self.stop = QtWidgets.QPushButton(Dialog)
        self.stop.setGeometry(QtCore.QRect(290, 250, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stop.setFont(font)
        self.stop.setStyleSheet("QPushButton{\n"
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
        self.stop.setDefault(False)
        self.stop.setObjectName("stop")
        self.otvet = QtWidgets.QLineEdit(Dialog)
        self.otvet.setGeometry(QtCore.QRect(80, 90, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.otvet.setFont(font)
        self.otvet.setStyleSheet("QLineEdit{\n"
"background-color:none;\n"
"border-style:solid;\n"
"border-width: 3px;\n"
"border-radius: 10px;\n"
"border-color: #3498db;\n"
"color:black;\n"
"}\n"
"QLineEdit:hover{\n"
"border-color:#2ecc71;\n"
"}")
        self.otvet.setText("")
        self.otvet.setObjectName("otvet")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 170, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
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
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ramz_ild"))
        self.digit.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\"></span></p><p><span style=\" color:#ffffff;\"><br/></span></p></body></html>"))
        self.question.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\"></span></p></body></html>"))
        self.stop.setText(_translate("Dialog", "Стоп"))
        self.pushButton.setText(_translate("Dialog", "Далее"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Testing()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
