import pickle,time

def clear():
    print('Очистка словаря')
    print('Внимание,это действие полностью очистит ваш словарь,'
    'вы хотите продолжить?')
    n = input('Введите да(если передумали,то нет): ')
    if n.lower() == 'да':
        print('Чищю словарь...')
        time.sleep(3)
        slovar.clear()
        print('Словарь  успешно очищен')
        with open('data.sav','wb') as f:
            pickle.dump(slovar,f)
        main()
    elif n.lower() == 'нет':
        main()
    else:
        print('Я не понимаю вас((')
def dell():
    const = 'Конец'
    print('Удаление слова')
    print('(Если вы закончили свою работу,введите Конец,для возврата в главное меню')
    print('Внимание:для удаления слова вам нужно ввести его английское значение')
    print('Например вы хотите удалить слово More')
    print('Вам нужно ввести именно More,а не его перевод!')
    print('Его нужно записать в точности как в словаре')
    print('Вот ваш словарь для удобства:')
    for key in slovar:
        print(key,'->',slovar[key])
    while True:
        n = input('Какое слово нужно удалить? ')
        n1 = n
        if n1.lower() == const.lower():
            main()
        else:
            try:
                slovar.pop(n)
                with open('data.sav','wb') as f:
                    pickle.dump(slovar,f)
                print('Слово удалено')
            except KeyError:
                print('Неверный ввод')

def add():
    const = 'Конец'
    print('Добавления слова')
    print('(Если вы закончили свою работу,введите Конец,для возврата в главное меню')
    while True:
        a = input('Какое новое английское слово вы хотите добавить: ')
        if str(a.lower()) == const.lower():
            main()
        else:
            b = input('Как оно переводиться?: ')
            if str(b.lower()) == const.lower():
                main()
            else:
                slovar[a]=b
                with open('data.sav','wb') as f:
                    pickle.dump(slovar,f)
                print('Готово)')

def main():
    print('Ваш текущий словарь:')
    for key in slovar:
        print(key,'->',slovar[key])
    print('В словаре',len(slovar),'слов' )
    print('Что вы хотите сделать?\n'
    'Добавить слово,удалить слово или полностью очистить словарь? ')
    while True:
        opr = input()
        if (opr.lower() == 'добавить') or (opr.lower() == 'добавить слово'):
            add()
        elif (opr.lower() == 'Удалить'.lower()) or (opr.lower() == 'удалить слово'):
            dell()
        elif opr.lower() == 'очистить словарь'.lower():
            clear()
        else:
            print('Я не знаю такую команду((.Попробуйте ещё раз')

def hello():
    print('Добро пожаловать в редактор словаря')
    time.sleep(1)
    print('Включаюсь...')
    time.sleep(3)

def start():
    global slovar
    hello()
    try:
        with open('data.sav','rb') as f:
            slovar = pickle.load(f)
            main()
    except FileNotFoundError:
        with open('data.sav','wb') as f:
            slovar = {}
            pickle.dump(slovar,f)
            main()

start()
