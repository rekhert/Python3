# Вклад в банке составляет x рублей.
# Ежегодно он увеличивается на p процентов, после
# чего дробная часть копеек отбрасывается.
# Каждый год сумма вклада становится больше.
# Определите, через сколько лет вклад составит не менее y рублей.
#
# Входные данные
# Программа получает на вход три натуральных числа: x, p, y.
#
# Выходные данные
# Программа должна вывести одно целое число.


x = int(input())
p = int(input())
y = int(input())

yearCount = 0

while x < y:
    x = float("{0:.2f}".format((x*(1+(p/100)))))
    yearCount += 1
print(yearCount)

