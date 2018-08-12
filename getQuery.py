import urllib.request
import json
url = 'http://data.fixer.io/api/latest?access_key=c5ce8bfc38506d2f66aed4fcf0847053&format=1'
req = urllib.request.Request(url)

##parsing response
r = urllib.request.urlopen(req).read()
cont = json.loads(r.decode('utf-8'))
rates = cont['rates']

def getcurrency(amount_money, currency_in, currency_out):

    if type(amount_money) != float and type(amount_money) != int:
        raise Exception("this is not float or int. please enter float")
    elif currency_in not in rates:
        raise Exception("currency not available")
    elif currency_out not in rates:
        raise Exception("currency not available")
    else:
        return amount_money*cont['rates'][currency_out] / cont['rates'][currency_in]

money = float(input('\n Введите сумму для перевода в другую валюту: '))
in1 = input('\n Введите валюту указанной суммы: ')
out1 = input('\n Введите валюту в которую нужно перевести сумму: ')
print('\n Конвертированная сумма: ', getcurrency(money, in1, out1))
