'''

задание А

Реализуйте функцию с возможностью отрпавить любое количество строк в качестве аргументов
которая будет их конкатинировать, убирать лишние пробелы, корректировать регистр по умолчанию.
Или в качестве альтернативы к каждой строке применять callback функцию со своим вариантом обработки строки.

func("this is", "a    funCtion\'s argUMents", "     simple Example" callback = lambda x: x )
"This is a funCtion's arguments simple example".

'''





def func(*ar):
    s = ""
    for i in ar:
        s += " " + i

    s = s.strip().capitalize()
    print(re.sub("\s\s+", " ", s))


func(" this is", "a    funCtion\'s argUMents", "     simple Example")