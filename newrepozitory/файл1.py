lst = [45, 444, 46, 666, 2, 3, 9, 90, 80, 4, 10]           # Линейный поиск
n = 890
index = 0
x = len(lst) - 1
while lst[index] != n and x > index:
    index += 1
if lst[index] == n:
    print(index)
else:
    print('Элемент не найден')