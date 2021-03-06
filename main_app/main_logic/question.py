from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Question(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(432, 381)
        font = QtGui.QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        Dialog.setStyleSheet("QDialog{\n"
"background-color:#34495e;\n"
"\n"
"}\n"
"")
        self.start = QtWidgets.QPushButton(Dialog)
        self.start.setGeometry(QtCore.QRect(110, 200, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.start.setFont(font)
        self.start.setStyleSheet("QPushButton{\n"
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
        self.start.setObjectName("start")
        self.name = QtWidgets.QLabel(Dialog)
        self.name.setGeometry(QtCore.QRect(20, -10, 411, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.question = QtWidgets.QLineEdit(Dialog)
        self.question.setGeometry(QtCore.QRect(110, 70, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.question.setFont(font)
        self.question.setStyleSheet("QLineEdit{\n"
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
        self.question.setObjectName("question")
        self.back = QtWidgets.QPushButton(Dialog)
        self.back.setGeometry(QtCore.QRect(140, 280, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.back.setFont(font)
        self.back.setStyleSheet("QPushButton{\n"
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
        self.back.setObjectName("back")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(100, 140, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("QComboBox{\n"
"background-color:none;\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ramz_ild"))
        self.start.setText(_translate("Dialog", "Старт"))
        self.name.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\">Сколько слов вы желаете повторить?</span></p></body></html>"))
        self.back.setText(_translate("Dialog", "Назад"))
        self.comboBox.setItemText(0, _translate("Dialog", "Свой словарь"))
        self.comboBox.setItemText(1, _translate("Dialog", "Словарь программы"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Question()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
