

#def getCurrencyRate(158.00, {"USD":"KZT"})

rates = {'USD': {'KZT': 360, 'RUB': 67, 'EUR': 0.87},
        'RUB': {'USD': 0.015, 'KZT': 5.4, 'EUR': 0.013},
        'EUR': {'KZT': 410, 'USD': 1.15, 'RUB': 76.6},
        'KZT': {'RUB': 0.19, 'USD': 0.003, 'EUR': 0.0024}}

def getcurrency(amount_money, currency_in, currency_out):

    if type(amount_money) != float and type(amount_money) != int:
        raise Exception("this is not float or int. please enter float")
    elif currency_in not in rates:
        raise Exception("currency not available")
    elif currency_out not in rates:
        raise Exception("currency not available")
    else:
        #print(amount_money*rates.get(currency_in).get(currency_out))
        return amount_money*rates.get(currency_in).get(currency_out)

amount_money = float(input('\n Введите сумму для перевода в другую валюту: '))
currency_in = input('\n Введите валюту указанной суммы (USD, KZT, RUB, EUR): ')
currency_out = input('\n Введите валюту в которую нужно перевести сумму (USD, KZT, RUB, EUR): ')
#getcurrency(amount_money, currency_in, currency_out)
print('\n Конвертированная сумма: ', getcurrency(amount_money, currency_in, currency_out))


