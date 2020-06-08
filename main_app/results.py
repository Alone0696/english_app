from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Results(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(733, 477)
        font = QtGui.QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        Dialog.setStyleSheet("QDialog{\n"
"background-color:#34495e;\n"
"\n"
"}\n"
"")
        self.again = QtWidgets.QPushButton(Dialog)
        self.again.setGeometry(QtCore.QRect(50, 370, 261, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.again.setFont(font)
        self.again.setStyleSheet("QPushButton{\n"
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
        self.again.setDefault(False)
        self.again.setObjectName("again")
        self.results = QtWidgets.QLabel(Dialog)
        self.results.setGeometry(QtCore.QRect(150, 10, 500, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.results.setFont(font)
        self.results.setStyleSheet("QLabel{\n"
"color:white;\n"
"}")
        self.results.setObjectName("results")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 70, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"color:white;\n"
"}")
        self.label.setObjectName("label")
        self.main_menu = QtWidgets.QPushButton(Dialog)
        self.main_menu.setGeometry(QtCore.QRect(400, 370, 261, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.main_menu.setFont(font)
        self.main_menu.setStyleSheet("QPushButton{\n"
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
        self.main_menu.setObjectName("main_menu")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(50, 110, 611, 251))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("QTextEdit{\n"
"background-color:none;\n"
"border-style:solid;\n"
"border-width: 3px;\n"
"border-radius: 10px;\n"
"border-color: #3498db;\n"
"color:black;\n"
"}\n"
"")
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ramz_ild"))
        self.again.setText(_translate("Dialog", "Пройти тест еще раз"))
        self.results.setText(_translate("Dialog", "Ваш результат"))
        self.label.setText(_translate("Dialog", "Ваши ошибки:"))
        self.main_menu.setText(_translate("Dialog", "В главное меню"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Results()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
