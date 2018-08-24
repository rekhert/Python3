
'''

Задание A
Напишите функцию которая будет конвертировать время
из 24 часового представления в 12 часовое представление с суффиксом AM
если это первая половина дня и PM если вторая

'''

time = input("Введите время в формате ЧЧ:ММ")
def timeconverter (time):
    h = int(time[:2])
    m = int(time[-2:])
    if h > 24 or h < 0:
        raise Exception ('ЧЧ не может превышать 24 или быть отрицательным')
    elif m > 59 or m < 0:
        raise Exception ('ММ не может превышать 59 или быть отрицательным')
    elif h >= 12:
        h -= 12
        z = 'PM'
    else:
        z = 'AM'
    print (h, ":", m , z)



timeconverter(time)

