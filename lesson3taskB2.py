#def getCurrencyRate(158.00, {"USD":"KZT"})
#
# Напишите
# метод, который
# вернет
# динамику
# курса
# валют
# за
# последние
# n
# дней.

exchange = {'USD': {'KZT': [356.80, 356.80, 354.06, 348.59, 348.82, 348.80, 349.76, 349.76, 349.76, 349.68, 348.21],
                    'RUB': [67.7061, 66.6899, 65.549, 63.5012, 63.7398, 63.3389, 63.3833, 63.0369, 62.5078, 62.2518],
                    'EUR': [0.8763, 0.8676, 0.8612, 0.8621, 0.8656, 0.8649, 0.8645, 0.8632, 0.8577, 0.8554]}}

def getcurrency(days, currency_in, currency_out):

    if days != int:
        raise Exception("this is not float or int. please enter float")
    elif days > 10:
        raise Exception("historical data for more than 10 days is not available")
    elif currency_in not in exchange:
        raise Exception("currency not available")
    elif currency_out not in exchange:
        raise Exception("currency not available")
    else:
        #print(amount_money*rates.get(currency_in).get(currency_out))
        return exchange.get(currency_in).get(currency_out[:days])

days = int(input('\n Введите кол-во дней: '))
currency_in = input('\n Введите валюту (USD, KZT, RUB, EUR): ')
currency_out = input('\n Введите валюту в которую нужно перевести сумму (USD, KZT, RUB, EUR): ')
#getcurrency(amount_money, currency_in, currency_out)
print('\n Конвертированная сумма: ', getcurrency(days, currency_in, currency_out))