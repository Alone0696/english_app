import configparser
import pickle
def clear():
    print('Очистка словаря')
    print('Внимание,это действие полность очистить ваш словарь,вы хотите продолжить?')
    n = input('Введите да(если передумали,то нет): ')
    if n.lower() == 'да':
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
    print('Вам нужно ввести его,а не его перевод!')
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
        a = input('Введите слово,что бы его доавбить: ')
        if str(a.lower()) == const.lower():
            main()
        else:
            b = input('Введите его перевод: ')
            if str(b.lower()) == const.lower():
                main()
            else:
                slovar[a]=b
                with open('data.sav','wb') as f:
                    pickle.dump(slovar,f)
                print('Готово')

def main():
    print('Добро пожаловать в редактор словаря')
    print('Ваш текущий словарь:')
    for key in slovar:
        print(key,'->',slovar[key])
    print('В словаре',len(slovar),'слов' )
    print('Что вы хотите сделать?Если добавить слово,введите:Добавить')
    print('Если хотите удалить слово,введите:Удалить')
    print('Если хотите выйти,просто закройте это окно.')
    print('Eсли вы хотите полность очистить словарь,введите:Очистка')
    while True:
        opr = input()
        if opr.lower() == 'Добавить'.lower():
            add()
        elif opr.lower() == 'Удалить'.lower():
            dell()
        elif opr.lower() == 'Очистка'.lower():
            clear()
        else:
            print('Я не знаю такую команду((.Попробуйте ещё раз')
try:
    with open('data.sav','rb') as f:
        slovar = pickle.load(f)
        main()
except FileNotFoundError:
    with open('data.sav','wb') as f:
        slovar = {}
        pickle.dump(slovar,f)
    main()