from random import randint

A = int(input('Enter size of the list:'))

random_list = []

i = 0

while i < A:

    random_list.append(randint(1, 100))

    i += 1

print(random_list)