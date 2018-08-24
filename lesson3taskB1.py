
#C2
# x = ['slovo1', 'slovo2']

# s = 'gde est slovo1'
#
# r = s.split()
#
# for word in r:
#     for mat in x:
#         if mat == word:
#              r[r.index(word)] = '***'
# s = " ".join(r)
# print(s)

#C2 alt

# x = {'slovo1' : 'drugoe slovo2']

# s = 'gde est slovo1'
#
# r = s.split()
#
# for word in r:
#     for mat in x:
#         if mat == word:
#              r[r.index(word)] = x[word]
# s = " ".join(r)
# print(s)

# перевод по такому то курсу B1
# try accept -- конструкция для отловкли ошибок API B1 with parcing



#
# task B2

# "KZT" : {"01-01-2018":356.9, "01-01-2018":356.9, "01-01-2018":356.9}
#import panddas as pd
#
#
# ds = {
# "USD": {
#   "KZT": [67.7061, 66.6899, 65.549, 65.549]
#   "RUB": [67.7061, 66.6899, 65.549, 65.549]
#   "USD": [67.7061, 66.6899, 65.549, 65.549]}
# "DATE": ["01-01-2018", "02-01-2018", "03-01-2018", "03-01-2018"] }
#
# def getRateLogByCurrency (C_from, C_to, days, current_date):
#     if current_date in ds.['DATE']:
#         dateIndex = ds['DATE'].index(current_date)
#         if c_from in ds and c_to in ds[c_from]:
#             result = ds.[c_from][dateIndex:(-1)*(days)]
#             return result
#
#
# print (getRateLogByCurrency("USD", "KZT", 2, "03-01-2018"))





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


