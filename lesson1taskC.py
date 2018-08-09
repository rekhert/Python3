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
