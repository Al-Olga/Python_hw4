"""Задайте натуральное число N. 
Напишите программу, которая составит список простых множителей числа N."""

print('Введите натуральное число: ')
n = int(input())
list_multipl = []
for i in range(1, n+1):
    list = []
    if n % i == 0:
        list.append(i)
        list.append(n//i)
        list_multipl.append(list)
print(list_multipl)
