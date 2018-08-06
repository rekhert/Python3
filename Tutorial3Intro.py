#Task_A

import math
pi = math.pi

print("\n Задание сложности a \n Реализуйте при помощи python формулу длинны окружности через радиус или диаметр.\n L=2πr или L=πD")

r = int(input('\n Введите радиус окружности: '))

if r < 0 or r == 0:
    print("\n Радиус окружности не может быть отрицательным, или равным нулю!\nВведите значение больше нуля")
    r = int(input('\n Введите радиус окружности: '))
    if r < 0 or r == 0:
        print("\n Радиус окружности не может быть отрицательным, или равным нулю! \nПереход к следующему заданию.")
    else: L1 = pi * 2 * r
    print("\n Длина окружности равна:", int(L1))
else:
    L1 = pi * 2 * r
    print("\n Длина окружности равна:", int(L1))


#Task_B

print("\n Задание сложности b \n Реализуйте при помощи python и библиотеки math (import math) формулу длины  окружности через площадь круга. \n L= 2√(s*π)")

s = int(input('\n Введите площадь окружности: '))

if s < 0 or s == 0:
    print("\n Площадь окружности не может быть отрицательной, или равной нулю!\nВведите значение больше нуля")
    s = int(input("\n Введите площадь окружности: "))
    if s < 0 or s == 0:
        print("\n Площадь окружности не может быть отрицательной, или равной нулю! \nПереход к следующему заданию.")
    else: L2 = 2 * math.sqrt(s * pi)
    print("\n Длина окружности равна:", int(L2))
else:
    L2 = 2 * math.sqrt(s * pi)
    print("\n Длина окружности равна:", int(L2))


#Task_C

print("\n Задание сложности с \n Реализуйте при помощи python и библиотеки math (import math) нахождение корней квадратного уравнения по формуле дискриминанта.  \n На всякий случай общая формула дискриминанта x1,2 =−b±√(b2−4ac)/ 2a")

a = int(input("\nВведите коэффициент a: "))

if a == 0:
    print("Коэффициэнт a в квадратном уравнении не может быть равным нулю. Введите коэффициент a, не равный нулю")
    a = int(input("\nВведите коэффициент a: "))
    if a == 0:
        print("Коэффициэнт a в квадратном уравнении не может быть равным нулю!")
    else:
        b = int(input("\nВведите коэффициент b: "))
        c = int(input("\nВведите коэффициент c: "))

D = b**2-4*a*c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print("\n 2 корня: \n корень 1",x1,"\n корень 2",x2)
elif D == 0:
    x = -b / (2 * a)
    print("\n один корень (дискриминант = 0): \n корень 1:", x)
else:
    print("\n Дискриминант =", D, "\n Квадратное уравнение не имеет корней (дискриминант < 0)")



