from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Add(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(561, 203)
        Dialog.setStyleSheet("QDialog{\n"
"background-color:#34495e;\n"
"}\n"
"")
        self.save = QtWidgets.QPushButton(Dialog)
        self.save.setGeometry(QtCore.QRect(430, 70, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.save.setFont(font)
        self.save.setStyleSheet("QPushButton{\n"
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
        self.save.setObjectName("save")
        self.original_l = QtWidgets.QLabel(Dialog)
        self.original_l.setGeometry(QtCore.QRect(20, 20, 231, 31))
        self.original_l.setObjectName("original_l")
        self.translate_l = QtWidgets.QLabel(Dialog)
        self.translate_l.setGeometry(QtCore.QRect(260, 20, 85, 31))
        self.translate_l.setObjectName("translate_l")
        self.original = QtWidgets.QLineEdit(Dialog)
        self.original.setGeometry(QtCore.QRect(20, 70, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.original.setFont(font)
        self.original.setStyleSheet("QLineEdit{\n"
"background-color:none;\n"
"border-style:solid;\n"
"border-width: 3px;\n"
"border-radius: 10px;\n"
"border-color: #3498db;\n"
"color:black;\n"
"}\n"
"")
        self.original.setText("")
        self.original.setObjectName("original")
        self.translate = QtWidgets.QLineEdit(Dialog)
        self.translate.setGeometry(QtCore.QRect(250, 70, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.translate.setFont(font)
        self.translate.setStyleSheet("QLineEdit{\n"
"background-color:none;\n"
"border-style:solid;\n"
"border-width: 3px;\n"
"border-radius: 10px;\n"
"border-color: #3498db;\n"
"color:black;\n"
"}\n"
"")
        self.translate.setObjectName("translate")
        self.status = QtWidgets.QLabel(Dialog)
        self.status.setGeometry(QtCore.QRect(420, 20, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.status.setFont(font)
        self.status.setStyleSheet("QLabel{color:white;}")
        self.status.setObjectName("status")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(260, 150, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("QCheckBox{\n"
"color:white;\n"
"}") 
        self.checkBox.setChecked(True)
        self.checkBox.setDisabled(True)
        self.checkBox.setObjectName("checkBox")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.save.setText(_translate("Dialog", "Добавить"))
        self.original_l.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Английское значение</span></p></body></html>"))
        self.translate_l.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Перевод</span></p></body></html>"))
        self.status.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\"></span></p></body></html>"))
        self.checkBox.setText(_translate("Dialog", "Auto Translate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Add()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
