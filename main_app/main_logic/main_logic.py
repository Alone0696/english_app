import sys,pickle,random,os
from googletrans import Translator
from PyQt5 import QtCore, QtGui, QtWidgets
from main_menu import Ui_MainWindow
from question import Ui_Question
from testing import Ui_Testing
from vnim import Ui_Vnim
from results import Ui_Results
from slovar import Ui_Slovar
from add import Ui_Add
from dell import Ui_Dell
from help import Ui_Help
from slovar_prog import Ui_Slovar_prog

def Testing_prog_slovar():
    global i,n,true,a,oshibki,verniy,k,slova,res,res_a,false
    slova,verniy,oshibki =[],[],[]
    k,true,false= 0,0,0
    i = 1
    window = QtWidgets.QDialog()
    ui = Ui_Testing()
    ui.setupUi(window)
    with open('big_data.sav','rb') as f:
        big_slovar = pickle.load(f)
    a = random.choice(list(big_slovar.keys()))
    ui.question.setText(a)
    ui.digit.setText(str(i))
    res_a = a
    res = big_slovar[a]
    del big_slovar[a]
    def check():
        global true,i,oshibki,verniy,k,slova,res_a,res,false
        a = random.choice(list(big_slovar.keys()))
        ui.question.setText(a)
        g = ui.otvet.text()
        i+=1
        ui.digit.setText(str(i))
        if res.lower() == g.lower():
            true+=1
        else:
            if g == '':
                oshibki.append('*Пустой ответ*')
                false+=1
            else:
                oshibki.append(g)
                false+=1
            slova.append(res_a)
            verniy.append(res)
            k+=1
        res = big_slovar[a]
        res_a = a
        del big_slovar[a]
        ui.otvet.setText('')
        if i == n+1:
            window.close()
            Results()
    
    def back():
        window.close()
        Question()
    ui.pushButton.setAutoDefault(True)
    ui.pushButton.setDefault(True)
    ui.pushButton.setFocus(True)
    ui.pushButton.clicked.connect(check)
    ui.stop.clicked.connect(back)
    window.show()
    window.exec_()

def Testing_polz_slovar():
    global i,n,true,a,oshibki,verniy,k,slova,res,res_a,false
    slova,verniy,oshibki =[],[],[]
    k,true,false= 0,0,0
    i = 1
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
    del slovar[a]
    def check():
        global true,i,oshibki,verniy,k,slova,res_a,res,false
        a = random.choice(list(slovar.keys()))
        ui.question.setText(a)
        g = ui.otvet.text()
        i+=1
        ui.digit.setText(str(i))
        if res.lower() == g.lower():
            true+=1
        else:
            if g == '':
                oshibki.append('*Пустой ответ*')
                false+=1
            else:
                oshibki.append(g)
                false+=1
            slova.append(res_a)
            verniy.append(res)
            k+=1
        res = slovar[a]
        res_a = a
        del slovar[a]
        ui.otvet.setText('')
        if i == n+1:
            window.close()
            Results()
    
    def back():
        window.close()
        Question()
    ui.pushButton.setAutoDefault(True)
    ui.pushButton.setDefault(True)
    ui.pushButton.setFocus(True)
    ui.pushButton.clicked.connect(check)
    ui.stop.clicked.connect(back)
    window.show()
    window.exec_()

def Results():
    global true,n,false
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
        if false == 0:
            ui.textEdit.setPlainText('Ошибок нет!Ты молодец)')
        else:
            for i in range(k):
                m = str(slova[i] + ' -> ' +'вы написали ' + str(oshibki[i]) + ',а правильно:'+ str(verniy[i]) + '\n')
                otvet = otvet + m
            ui.textEdit.setPlainText(otvet)
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
    with open('big_data.sav','rb') as h:
        big_slovar = pickle.load(h)
    MainWindow.close()
    def back():
        window.close()
        MainWindow.show()
    def start():
        global n
        try:
            n = int(ui.question.text())
            if n <= 0:
                ui.question.setText("Некорректно")
            elif ui.comboBox.currentText() == 'Свой словарь':
                if n > len(slovar)-1:
                    ui.question.setText("В словаре нет столько слов(")
                else:
                    window.close()
                    Testing_polz_slovar()
            elif ui.comboBox.currentText() == 'Словарь программы':
                if n > len(big_slovar)-1:
                    ui.question.setText("В словаре нет столько слов(")
                else:
                    window.close()
                    Testing_prog_slovar()
        except ValueError:
            ui.question.setText('Неверно')
    ui.back.clicked.connect(back)
    ui.question.setFocus(True)
    ui.start.setAutoDefault(True)
    ui.start.setDefault(True)
    ui.start.clicked.connect(start)
    window.show()
    window.exec_()

def Slovar():
    def main():
        window_sl  = QtWidgets.QDialog()
        ui = Ui_Slovar()
        ui.setupUi(window_sl)
        MainWindow.close()
        with open('data.sav','rb') as f:
            slovar = pickle.load(f)
        with open('big_data.sav','rb') as h:
            big_slovar = pickle.load(h)
        def show_prog_slovar():
            window = QtWidgets.QDialog()
            ui = Ui_Slovar_prog()
            ui.setupUi(window)
            def show_in():
                d = ''
                for key in big_slovar:
                    d+= str(key) + ' -> ' + str(big_slovar[key]) + '\n'
                ui.window_s.setPlainText(d)
            show_in()
            window.show()
            window.exec_()
        def return_mainmenu():
            window_sl.close()
            MainWindow.show()
        def show_slovar():
            d = ''
            for key in slovar:
                d+= str(key) + ' -> ' + str(slovar[key]) + '\n'
            ui.window_s.setPlainText(d)
        def add():
            window = QtWidgets.QDialog()
            ui = Ui_Add()
            ui.setupUi(window)
            def add_in():
                a = ui.original.text()
                b = ui.translate.text()
                if a == '' and b == '':
                    ui.status.setText('Пустой ввод')
                elif b=='':
                    tr = Translator()
                    rs = tr.translate(f'{a}',src='en',dest='ru')
                    slovar[a] = rs.text
                    with open('data.sav','wb') as f:
                        pickle.dump(slovar,f)
                    ui.status.setText('Успешно')
                    ui.original.setText('')
                    ui.translate.setText('')
                    show_slovar()
                elif b !='':
                    slovar[a]=b
                    with open('data.sav','wb') as f:
                        pickle.dump(slovar,f)
                    ui.status.setText('Успешно')
                    ui.original.setText('')
                    ui.translate.setText('')
                    show_slovar()
            ui.save.clicked.connect(add_in)
            window.show()
            window.exec_()
        def dell():
            window = QtWidgets.QDialog()
            ui = Ui_Dell()
            ui.setupUi(window)
            def dell_in():
                try:
                    a = ui.slovo.text()
                    slovar.pop(a)
                    ui.status.setText('Успешно')
                    with open('data.sav','wb') as f:
                        pickle.dump(slovar,f)
                    show_slovar()
                    ui.slovo.setText('')
                except KeyError:
                    ui.slovo.setText('Неверно')
            ui.dell.clicked.connect(dell_in)
            window.show()
            window.exec_()
        window_sl.show()
        show_slovar()
        ui.main_m.clicked.connect(return_mainmenu)
        ui.add.clicked.connect(add)
        ui.dell.clicked.connect(dell)
        ui.dell_2.clicked.connect(show_prog_slovar)
        window_sl.exec_()
    def check_slovar_in():
        global f
        try:
            open('data.sav','rb')
            main()
        except FileNotFoundError:
            with open('data.sav','wb') as f:
                slovar = {}
                pickle.dump(slovar,f)
                f.close()
                main()
    check_slovar_in()       

def Help():
    window = QtWidgets.QDialog()
    ui = Ui_Help()
    ui.setupUi(window)
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
ui.settings.clicked.connect(Slovar)
ui.start.clicked.connect(check_slovar)
ui.help.setDisabled(True)
#ui.help.clicked.connect(Help)
sys.exit(app.exec_())
