'''
Задание B
Напишите функцию которая считает количество
обпределенного слова или словосочитания в заданном тексте
'''

text = input('Введите текст')
word = input('Введите слово')

def countword(text, word):

    if len(text) == 0:
        raise Exception ('Текс не может быть пуст')
    elif len(word) == 0 :
        raise Exception ('Слово не может быть пустым')
    print (text.count(word))

countword(text, word)