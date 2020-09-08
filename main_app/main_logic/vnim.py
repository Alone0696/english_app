from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Vnim(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(737, 262)
        Dialog.setStyleSheet("QDialog{\n"
"background-color:#34495e;\n"
"\n"
"}\n"
"")
        self.ok = QtWidgets.QPushButton(Dialog)
        self.ok.setGeometry(QtCore.QRect(230, 160, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ok.setFont(font)
        self.ok.setStyleSheet("QPushButton{\n"
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
        self.ok.setObjectName("again")
        self.results = QtWidgets.QLabel(Dialog)
        self.results.setGeometry(QtCore.QRect(20, 10, 701, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.results.setFont(font)
        self.results.setStyleSheet("")
        self.results.setObjectName("results")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ramz_ild"))
        self.ok.setText(_translate("Dialog", "Хорошо"))
        self.results.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\">Я не нашел словари((Возможно вы в первый раз запустили эту программу)</span></p><p><span style=\" color:#ffffff;\">Нажмите на кнопку \'Редактировать словарь\' и создайте свой первый словарь!!</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Vnim()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
