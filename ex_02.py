"""Задайте натуральное число N. 
Напишите программу, которая составит список простых множителей числа N."""

print('Введите натуральное число: ')
n = int(input())
if n > 1:
    list_multipl = []
    for i in range(2, n+1):
        if n % i == 0:
            count = 0
            for j in range(2, i // 2+1):
                if i % j == 0:
                    count += 1
            if count <= 0:
                list_multipl.append(i)
    print(list_multipl)