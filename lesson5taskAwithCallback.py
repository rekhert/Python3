'''
задание А

Реализуйте функцию с возможностью отрпавить любое количество строк в качестве аргументов
которая будет их конкатинировать, убирать лишние пробелы, корректировать регистр по умолчанию.
Или в качестве альтернативы к каждой строке применять callback функцию со своим вариантом обработки строки.

func("this is", "a    funCtion\'s argUMents", "     simple Example" callback = lambda x: x )
"This is a funCtion's arguments simple example".

'''



# def main(*string):
#     tmp = []
#     for s in string:
#         tempString = s.split()
#         tmp.append(" ".join(tempString))
#     return " ".join(tmp).capitalize()

def userMethod(s):
    return s+"___"

def main(*string, stringMethod = None):
    tmp = []
    for s in string:
        if stringMethod is not None:
            s = stringMethod(s)
            tmp.append(s)

        else:
            tempString = s.split()
            tmp.append(" ".join(tempString))
    return " ".join(tmp).capitalize()


#main("this is", "a    funCtion\'s argUMents","this is", "a    funCtion\'s argUMents", stringMethod=lambda s: s+"----")

# упаковка и распаковка аргументов:
# def func(*args):
#     print(args)
#     print(*args)

#аргументы по ключ слову и вариативные
# def func(s1, s2):
#     print(s1, s2)
#
#
# func("a", "b")
# a
# b
#
#
# def func(s1="", s2=""):
#     print(s1, s2)
#
#
# func("a", "b")
# a
# b
# func(s2="a", s1="b")
# b
# a
# func(s1="a", s2="b")
# a
# b
#
#
# def func(**kwargs):
#     print(kwargs)
#
#
# func(s1="a", s2="b")
# {'s1': 'a', 's2': 'b'}
# func(s1="a", s2="b", callback="")
# {'s1': 'a', 's2': 'b', 'callback': ''}
# func(s1="a", s2="b", s3="")
# {'s1': 'a', 's2': 'b', 's3': ''}





