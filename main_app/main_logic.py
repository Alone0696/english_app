from PyQt5 import QtCore, QtGui, QtWidgets
from main_menu import Ui_MainWindow
from question import Ui_Question
from testing import Ui_Testing
from vnim import Ui_Vnim
from results import Ui_Results
import sys,pickle,random,os

def Testing():
    global i,n,true,res,a,oshibki,verniy,k,res_a,slova
    slova = []
    oshibki = []
    verniy = []
    k = 0
    i = 1
    true = 0
    window = QtWidgets.QDialog()
    ui = Ui_Testing()
    ui.setupUi(window)
    with open('data.sav','rb') as f:
        slovar = pickle.load(f)
    a = random.choice(list(slovar.keys()))
    ui.question.setText(a)
    ui.digit.setText(str(i))
    res_a = a
    res = slovar[a]
    #verniy.append(slo)
    del slovar[a]
    def check():
        global res,true,i,a,n,oshibki,verniy,k,res_a,slova
        a = random.choice(list(slovar.keys()))
        ui.question.setText(a)
        g = ui.otvet.text()
        i+=1
        ui.digit.setText(str(i))
        if res.lower() == g.lower():
            true+=1
        else:
            oshibki.append(g)
            slova.append(res_a)
            verniy.append(res)
            k+=1
        res = slovar[a]
        res_a = a
        del slovar[a]
        ui.otvet.setText('')
        def i_check():
            global i,n
            if i == n+1:
                window.close()
                Results() 
        i_check()   
    def back():
        Question()
        window.close()
    ui.pushButton.setAutoDefault(True)
    ui.pushButton.setDefault(True)
    ui.pushButton.setFocus(True)
    ui.pushButton.clicked.connect(check)
    ui.stop.clicked.connect(back)
    window.show()
    window.exec_()

def Results():
    global true,n
    window = QtWidgets.QDialog()
    ui = Ui_Results()
    ui.setupUi(window)
    def done():
        global true,n
        true = str(true)
        n = str(n)
        d = 'Ваш результат: ' + true + ' правильных из ' + n + '.'
        ui.results.setText(d)
        otvet = ''
        for i in range(k):
            m = str(slova[i] + ' -> ' + str(oshibki[i]) + ',а правильно:'+ str(verniy[i]) + '\n')
            otvet = otvet + m
        font = QtGui.QFont()
        font.setPointSize(13)
        ui.textEdit.setFont(font)
        ui.textEdit.setPlainText(otvet)
        ui.textEdit.setReadOnly(True)
        def main_menu():
            window.close()
            MainWindow.show()
        def again_test():
            window.close()
            Question()
        ui.main_menu.clicked.connect(main_menu)
        ui.again.clicked.connect(again_test)
    window.show()
    done()
    window.exec_()

def Vnim():
    window = QtWidgets.QDialog()
    ui = Ui_Vnim()
    ui.setupUi(window)
    def okey():
        window.close()
    ui.ok.clicked.connect(okey)
    window.show()
    window.exec_()

def Question():
    global n 
    window = QtWidgets.QDialog()
    ui = Ui_Question()
    ui.setupUi(window)
    with open('data.sav','rb') as f:
        slovar = pickle.load(f)
    MainWindow.close()
    def back():
        window.close()
        MainWindow.show()
    def start():
        global n
        try:
            n = int(ui.question.text())
            if n > len(slovar)-1:
                ui.question.setText("В словаре нет столько слов(")
            else:
                window.close()
                Testing()
        except ValueError:
            ui.question.setText('Неверно')
    ui.back.clicked.connect(back)
    ui.question.setFocus(True)
    ui.start.setAutoDefault(True)
    ui.start.setDefault(True)
    ui.start.clicked.connect(start)
    window.show()
    window.exec_()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
def check_slovar():
    try:
        open('data.sav','rb')
        Question()
    except FileNotFoundError:
        Vnim()
def slovar():
    os.startfile('logic_data.exe')
ui.settings.clicked.connect(slovar)
ui.start.clicked.connect(check_slovar)
sys.exit(app.exec_())
