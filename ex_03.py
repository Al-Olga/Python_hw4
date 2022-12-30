"""Задайте последовательность чисел. Напишите программу, которая выведет список
 неповторяющихся элементов исходной последовательности."""

import random
list1 = []
print('Введите количество элементов: ')
n = int(input())
for _ in range(n):
    list1.append(random.randint(0, 5))
print('исходный список: ', list1)

list2 = []
for i in range(0, (len(list1))):
    temp = list1[i]
    count = 0
    for j in range(0, (len(list1))):
        if temp == list1[j]:
            count += 1
            if count == 2:
                break
    else:
        list2.append(list1[i])
print('список неповторяющихся элементов: ',list2)
