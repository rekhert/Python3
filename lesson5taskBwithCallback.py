'''
Задание B
При помощи вашей новой функции из задания А и callback функции сделайте так чтобы ваша функция
находила все url адреса в тексте и оборачивала их в <a href="{url}">{text}</a>
func("на сайте http://host.com можно найти полезные материалы", callback)
В результате получим
"На сайте <a href="http://host.com">http://host.com</a> можно найти полезные материалы"
'''

import re
def linkMethod(s):
    # tempstring = s.split()
    lst = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', s)
    # for n, i in enumerate(tempstring):
    #    if i == 'http':
    #        tempstring[n] = 10
    for i in lst:
        html = "<a href=\""+i+"\">"+i+"</a>"
        s=s.replace(i, html)
    print(s)

    # for s in tempstring:
    #     if s == "http":
    #         html = "<a href=\"" + s + "\">" + s + "</a>"
    #         s = s.replace(s, html)
    #     tempstring.append(s)
    # return " ".join(tempstring).capitalize()

# linkMethod("на сайте http://host.com можно найти полезные материалы")


def main(*string, stringmethod = None):
    tmp = []
    for s in string:
        if stringmethod is not None:
            s = stringmethod(s)
            tmp.append(s)
        else:
            tempstring = s.split()
            tmp.append(" ".join(tempstring))
    return tmp
        # " ".join(tmp).capitalize()
main("на сайте http://host.com можно найти полезные материалы", stringmethod = linkMethod)
