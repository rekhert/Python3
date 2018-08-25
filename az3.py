'''
Вводится число n, после него вводится еще n чисел.
Найти сореднее арифметическое
максимум
'''

import sys

n = int(input("enter number"))
summ = 0
maxn = -sys.maxsize -1

for i in range(n):
    x = int(input())
    if x > maxn:
        maxn = x
    summ +=x
print(summ/x,maxn)
