# дата сет отношений валют
sourceDataSet = {
    "USD": {
        "KZT" : [356.80, 356.80, 354.06, 348.59, 348.82, 348.80, 349.76, 349.76, 349.76, 349.68, 348.21],
        "USD" : [356.80, 356.80, 354.06, 348.59, 348.82, 348.80, 349.76, 349.76, 349.76, 349.68, 348.21],
        "EUR" : [356.80, 356.80, 354.06, 348.59, 348.82, 348.80, 349.76, 349.76, 349.76, 349.68, 348.21],
    },
    "DATE": ['01-01-2018', '02-01-2018', '03-01-2018', '04-01-2018','05-01-2018','06-01-2018','07-01-2018','08-01-2018','09-01-2018']
}



def getRateLogByCurrency(currencyFrom, currencyTo, days, current_date):
    '''
    метод получает лог изменения курса одной валюты к другой
    за n дней по указанну дату включительно
    :param currencyFrom: str Валюта по отношению к которой нужен курс
    :param currencyTo: str Валюта курс которой нужен
    :param days: int период
    :param current_date: str текущая дата
    :return: dict
    '''
    if current_date in sourceDataSet['DATE']:
        dateIndex = sourceDataSet['DATE'].index(current_date)

        if currencyFrom in sourceDataSet and currencyTo in sourceDataSet[currencyFrom]:
            start_index = dateIndex - days
            end_index   = dateIndex+1

            if start_index < 0 : start_index = 0

            dataSet         = {'rate':[],'date':[]}
            dataSet['rate'] = sourceDataSet[currencyFrom][currencyTo][start_index:end_index]
            dataSet['date'] = sourceDataSet['DATE'][start_index:end_index]

            return dataSet


def printCurrencyLog(data):
    '''
    метод выводит данные по истории курса валют в отформатированной таблице
    :param data: dict данные метода getRateLogByCurrency
    '''

    word  = "{:15}|" # формат для строки
    money = "{:15.2f}|" # формат для денег

    print("|",word.format("date"), word.format("rate"))
    print("|",word.format("---------------"), word.format("---------------"))

    for i in range(len(data['date'])-1):
        print("|",word.format(data['date'][i]), money.format(data['rate'][i]))


printCurrencyLog(getRateLogByCurrency("USD", "KZT", 3, '08-01-2018'))
