
'''

Задание B

При помощи вашей новой функции из задания А и callback функции сделайте так чтобы ваша функция
находила все url адреса в тексте и оборачивала их в <a href="{url}">{text}</a>

func("на сайте http://host.com можно найти полезные материалы", callback)
В результате получим
"На сайте <a href="http://host.com">http://host.com</a> можно найти полезные материалы"

'''


import re
def func (s):
    lst = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', s)

    for i in lst:
        html = "<a href=\""+i+"\">"+i+"</a>"
        s=s.replace(i, html)

    print(s)



func("на сайте http://host.com можно найти полезные материалы")