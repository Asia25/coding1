def coins_for_change():
    """ Эта программа считает монетки на сдачу для российских купюр номиналом от 1 рубля  до 5000 рублей
        и выводит пошагово номинал каждой купюры или монеты для сдачи, а в конце подсчитывает общее
        количество монет для сдачи, так же в ней присутствует исключение пользовательского ввода
        surrender - Сдача """
    while True:   # Исключения пользовательсокого ввода
        try:
            surrender = int(input('Extra money:'))  # Пользователь вводит размер сдачи
            if 0 < surrender:
                break
            else:
                raise ValueError
        except ValueError:
            print('Введите целое число больше нуля')
    banknote_1 = 5000            # Номинал купюр и монет на поясе у кассира
    banknote_2 = 1000
    banknote_3 = 500
    banknote_4 = 100
    banknote_5 = 50
    coin_1 = 10
    coin_2 = 5
    coin_3 = 2
    coin_4 = 1
    number_of_banknote_or_coins = 0
    while surrender != 0:             # Основной код
        if surrender >= banknote_1:
            surrender -= banknote_1
            number_of_banknote_or_coins += 1
            print(banknote_1)
        elif surrender >= banknote_2:
            surrender -= banknote_2
            number_of_banknote_or_coins += 1
            print(banknote_2)
        elif surrender >= banknote_3:
            surrender -= banknote_3
            number_of_banknote_or_coins += 1
            print(banknote_3)
        elif surrender >= banknote_4:
            surrender -= banknote_4
            number_of_banknote_or_coins += 1
            print(banknote_4)
        elif surrender >= banknote_5:
            surrender -= banknote_5
            number_of_banknote_or_coins += 1
            print(banknote_5)
        elif surrender >= coin_1:
            surrender -= coin_1
            number_of_banknote_or_coins += 1
            print(coin_1)
        elif surrender >= coin_2:
            surrender -= coin_2
            number_of_banknote_or_coins += 1
            print(coin_2)
        elif surrender >= coin_3:
            surrender -= coin_3
            number_of_banknote_or_coins += 1
            print(coin_3)
        elif surrender >= coin_4:
            surrender -= coin_4
            number_of_banknote_or_coins += 1
            print(coin_4)
    return 'Number of banknote or coins for change: ' + str(number_of_banknote_or_coins)


print(coins_for_change())