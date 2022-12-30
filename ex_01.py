"""Вычислить число π c заданной точностью d

Пример:
- при $d = 0.0001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$"""

import math
print('Введите необходимую точность: ')
n = float(input())
count = 0
while round(n) != 1:
    n *= 10
    count += 1
print(round(math.pi,count))