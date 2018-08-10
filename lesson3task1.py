

#def getCurrencyRate(158.00, {"USD":"KZT"})

rates =  {'USD':{'KZT':360, 'RUB':67, 'EUR':0.87},
        'RUB':{'USD':0.015,'KZT':5.4, 'EUR':0.013},
        'EUR':{'KZT':410, 'USD':1.15, 'RUB':76.6},
        'KZT':{'RUB':0.19, 'USD':0.003, 'EUR':0.0024}}


def getcurrency(amount_money, currency_in, currency_out):
    if type(amount_money) != float:
        raise Exception("this is not float. please enter float")
    else:
        if currency_in not in rates:
            raise Exception("currency not in list")

