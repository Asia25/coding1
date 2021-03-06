#                                        ЛИНЕЙНЫЙ ПОИСК

# Линейный поиск осуществляется из списка элементов введенных нами (количество элементов ограниченно 10-ю)

# Линейный поиск выводит индекс искомого нами элемента





def linear_search(number):

    lst = [int(input('1)Введите число:')), int(input('2)Введите число:')), int(input('3)Введите число:')),

           int(input('4)Введите число:')), int(input('5)Введите число:')), int(input('6)Введите число:')),

           int(input('7)Введите число:')), int(input('8)Введите число:')), int(input('9)Введите число:')),

           int(input('10)Введите число:'))]  # Ввод в список 10-ти значений

    index = 0

    x = len(lst) - 1

    while lst[index] != number and x > index:  # В данном циле проводится перебор каждого элемента по порядку

        index += 1

    if lst[index] == number:  # Если элемент равен искомому - выводим его индекс

        return 'Индекс:', index

    else:  # В противном случае - выводим "Элемент не найден"

        return 'Элемент не найден'





#                                        БИНАРНЫЙ ПОИСК

# Бинарный поиск осуществляется из саписка элементов введенных нами(количество элементов ограничено 10-ю)

# Бинарный поиск выводит индекс искомого нами элемента





def binary_search(number):

    lst = [int(input('1)Введите число:')), int(input('2)Введите число:')), int(input('3)Введите число:')),

           int(input('4)Введите число:')), int(input('5)Введите число:')), int(input('6)Введите число:')),

           int(input('7)Введите число:')), int(input('8)Введите число:')), int(input('9)Введите число:')),

           int(input('10)Введите число:'))]  # Ввод в список 10-и значений

    left = 0  # Обозначаем индекс левого элемента как 0

    right = len(lst)  # Обозначаем индекс правого элемента как длинну списка

    while left < right - 1:  # В данном цикле мы отбрасываем все значения кроме двух,один из которых - искомой элемент

        mid = (left + right) // 2

        if lst[mid] > number:

            right = mid

        else:

            left = mid

    if lst[left] == number:  # Если левая граница равна искомому элементу - выводим её индекс на экран

        return 'Индекс:', left

    elif lst[right] != number:  # Если же правая граница не равна искомому элементу - выводим "Элемент не найден"

        return 'Элемент не найден'

    else:  # В остальном - выводим индекс правой границы

        return 'Индекс:', right





#                                        CОРТИРОВКА ВЫБОРОМ





def sort_by_selection(lst):

    # в переменной k хранится индекс элемента, подлежащего обмену (двигаемся слева на право)



    k = 0

    while k < len(lst) - 1:  # -1, т.к. последний элемент обменивать уже не надо

        m = k  # в m хранится минимальное значение

        i = k + 1  # откуда начинать поиск минимума (элемент следующий за k)

        while i < len(lst):

            if lst[i] < lst[m]:

                m = i

            i += 1

        t = lst[k]

        lst[k] = lst[m]

        lst[m] = t

        k += 1  # переходим к следующему значению для обмена

    return lst