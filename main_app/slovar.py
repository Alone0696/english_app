from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Slovar(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(795, 363)
        Dialog.setStyleSheet("QDialog{\n"
"background-color:#34495e;\n"
"}\n"
"")
        self.window_s = QtWidgets.QTextEdit(Dialog)
        self.window_s.setGeometry(QtCore.QRect(30, 30, 731, 241))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.window_s.setFont(font)
        self.window_s.setReadOnly(True)
        self.window_s.setStyleSheet("QTextEdit{\n"
"background-color:none;\n"
"border-style:solid;\n"
"border-width: 3px;\n"
"border-radius: 10px;\n"
"border-color: #3498db;\n"
"color:black;\n"
"}\n"
"")
        self.window_s.setObjectName("window_s")
        self.dell = QtWidgets.QPushButton(Dialog)
        self.dell.setGeometry(QtCore.QRect(220, 280, 171, 71))
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
        self.main_m = QtWidgets.QPushButton(Dialog)
        self.main_m.setGeometry(QtCore.QRect(590, 280, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.main_m.setFont(font)
        self.main_m.setStyleSheet("QPushButton{\n"
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
        self.main_m.setObjectName("main_m")
        self.add = QtWidgets.QPushButton(Dialog)
        self.add.setGeometry(QtCore.QRect(30, 280, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add.setFont(font)
        self.add.setStyleSheet("QPushButton{\n"
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
        self.add.setObjectName("add")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ramz_ild"))
        self.window_s.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.dell.setText(_translate("Dialog", "Удалить"))
        self.main_m.setText(_translate("Dialog", "В главное меню"))
        self.add.setText(_translate("Dialog", "Добавить"))


