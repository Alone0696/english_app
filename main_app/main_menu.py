from PyQt5 import QtCore, QtGui, QtWidgets
import sys,pickle,random,os
from question import Ui_Question
from  testing import Ui_Testing
from vnim import Ui_Vnim
from results import Ui_Results
class Ui_MainWindow(object):
    def results(self):
        global true,n
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Results()
        self.ui.setupUi(self.window)
        self.window.show()
        ui = Ui_MainWindow()
        def done():
            global true,n
            true = str(true)
            n = str(n)
            a = 'Ваш результат: '
            b = ' правильных из '
            c = '.'
            d = a + true + b + n + c
            self.ui.results.setText(d)
            otvet = ''
            for i in range(k):
                m = str(verniy[i]) + ' -> ' + str(oshibki[i]) + '\n'
                otvet = otvet + m
            self.ui.textEdit.setPlainText(otvet)
        def main_menu():
            self.window.close()
            MainWindow.show()
        def again_test():
            self.window.close()
            ui.question()
        done()
        self.ui.main_menu.clicked.connect(main_menu)
        self.ui.again.clicked.connect(again_test)
    def vnim(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Vnim()
        self.ui.setupUi(self.window)
        self.window.show()
        def okey():
            self.window.close()
        self.ui.ok.clicked.connect(okey)
    def testing(self):
        global i,n,true,res,a,oshibki,verniy,k,res_a
        oshibki = []
        verniy = []
        k = 0
        i = 1
        true = 0
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Testing()
        self.ui.setupUi(self.window)
        self.window.show()
        ui = Ui_MainWindow()
        with open('data.sav','rb') as f:
            slovar = pickle.load(f)
        a = random.choice(list(slovar.keys()))
        self.ui.question.setText(a)
        self.ui.digit.setText(str(i))
        res_a = a
        res = slovar[a]
        del slovar[a]
        def check():
            global res,true,i,a,n,oshibki,verniy,k,res_a
            a = random.choice(list(slovar.keys()))
            self.ui.question.setText(a)
            g = self.ui.otvet.text()
            i+=1
            self.ui.digit.setText(str(i))
            if res.lower() == g.lower():
                true+=1
            else:
                oshibki.append(g)
                verniy.append(res_a)
                k+=1
            res = slovar[a]
            res_a = a
            del slovar[a]
            self.ui.otvet.setText('')
            def i_check():
                global i,n
                if i == n+1:
                    self.window.close()
                    ui.results()
            i_check()
        def back():
            ui.question()
            self.window.close()
        self.ui.pushButton.setAutoDefault(True)
        self.ui.pushButton.setDefault(True)
        self.ui.pushButton.setFocus(True)
        self.ui.pushButton.clicked.connect(check)
        self.ui.stop.clicked.connect(back)
    def question(self):
        global n
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Question()
        self.ui.setupUi(self.window)
        self.window.show()
        ui = Ui_MainWindow()
        with open('data.sav','rb') as f:
            slovar = pickle.load(f)
        MainWindow.close()
        def back():
            self.window.close()
            MainWindow.show()
        def start():
            global n
            try:
                n = int(self.ui.question.text())
                if n > len(slovar)-1:
                    self.ui.question.setText('В словаре нет столько слов(')
                else:
                    self.window.close()
                    ui.testing()
            except ValueError:
                self.ui.question.setText('Неверно')
        self.ui.back.clicked.connect(back)
        self.ui.question.setFocus(True)
        self.ui.start.clicked.connect(start)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 400)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
"background-color:#34495e;\n"
"\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(150, 130, 186, 71))
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
        self.settings = QtWidgets.QPushButton(self.centralwidget)
        self.settings.setGeometry(QtCore.QRect(130, 230, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.settings.setFont(font)
        self.settings.setStyleSheet("QPushButton{\n"
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
        self.settings.setObjectName("settings")
        self.help = QtWidgets.QPushButton(self.centralwidget)
        self.help.setGeometry(QtCore.QRect(380, 320, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.help.setFont(font)
        self.help.setStyleSheet("QPushButton{\n"
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
        self.help.setObjectName("help")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(60, 70, 391, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.name.setFont(font)
        self.name.setObjectName("name")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ramz_ild"))
        self.start.setText(_translate("MainWindow", "Начать"))
        self.settings.setText(_translate("MainWindow", "Редактировать словарь"))
        self.help.setText(_translate("MainWindow", "Помощь"))
        self.name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Тренажер для запоминания слов</span></p></body></html>"))



import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
def check_slovar():
    try:
        with open('data.sav','rb') as f:
            slovar = pickle.load(f)
        ui.question()
    except FileNotFoundError:
        ui.vnim()
def slovar():
    os.startfile('logic_data.exe')
ui.settings.clicked.connect(slovar) 
ui.start.clicked.connect(check_slovar)
sys.exit(app.exec_())
