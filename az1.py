
'''
Напиши программу

Где вводятся по очереди числа пока не введется ноль.
После ноля вывести количество всех чисел и сколько среди них четных

добавить максимум и минимум
второй максимум

'''

a = int(input('введите число'))
list = []
count = 0
even_count = 0
mina = a
maxa = a
maxa2 = a
while a != 0:
    count += 1
    list.append(a)
    if a % 2 == 0:
        even_count += 1
    if a < mina:
        mina = a
    if a > maxa:
        max2 = maxa
        maxa = a
    elif a > maxa2:
        maxa2 = a
    a = int(input('введите число'))
else:
    print("введен ноль, цикл остановлен", "\n кол-во введенных чисел до нуля:", count, "\n кол-во четных:", even_count,
    "\n минимум", min(list), mina, "\n максимум", max(list), maxa, "\n второй макс:", max2)


