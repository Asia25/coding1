def steps_of_the_pyramid():

    index = 0

    while True:   # Исключения пользовательсокого ввода

        try:

            height = int(input('height:'))

            if 0 < height < 24:

                break

            else:

                raise ValueError

        except ValueError:

            print('Введите целое число от 1 до 23')



    while index != height:  # Основной код

        index += 1

        if index > 1:

            element = ' ' * (height - (index - 1))

            element += '#' * index

            print(element)

        if index == height:

            element = '#' * (height + 1)

            return element

        elif index == 1:      # Выравниваю правый столбец в зависимости от того двузначное или однозначное число

            if height < 10:   # Проверка на однозначность

                element = ' ' * (height - (index - 1))

                element += str(height)

                print(element)

            elif height >= 10:    # Проверка на двузначность

                element = ' ' * (height - index)

                element += str(height)

                print(element)





print(steps_of_the_pyramid())