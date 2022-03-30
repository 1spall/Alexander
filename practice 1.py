catalog = ['Мяч', 'сетку' 'кроссовки']
print('добрый день вас приветствует магазин спорт-товаров')
print('1-Посмотреть каталог')
choice = input('Введите ваш выбор')
if choice == '1':
    print('Каталог: ')
    for item in enumerate(catalog):
        print(f'{item[0]+1}-{item[1]}')
        choice_item = input('Введите товар:')
        print(f'Этот товар стоит: {prices[int(choice_item)-1]}')
        last_question == 'д' or last_question == 'да':
        print(f'вы купили {catalog[int(choice_item)-1]}) за {prices[int(choice_item)]-1]}')
        cart.append(int(choice_item)-1)
        if choice == '2'
        print('Корзина: ')
        sum1 = 0
        for i in cart:
            print
        sum1 += prices[i]
