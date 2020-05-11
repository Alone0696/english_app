def check():
    import random
    slovar = {'More':'Много','Example':'Пример','Test':'Тест','Water':'Вода'}
    run = slovar
    for i in range(len(run)):
        a = random.choice(list(run.keys()))
        print(a)
        b = str(run[a])
        n = str(input())
        del run[a]
        if b.lower() == n.lower():
            print('True')
        else:
            print('False')
slovar = {'More':'Много','Example':'Пример','Test':'Тест','Water':'Вода'}
check()