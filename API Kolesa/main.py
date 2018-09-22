

#домашка -- перенести все в отдельный проект



#создаем readme
#создаем main.py
#создаем виртуальное окружение
#pip freeze requirements.txt


#========================================
#метод получения данных объявлений по id
#метод получения уникальных id из данных объявлений
#метод создающий финальную структуру


#========================================
#принцип single responsibility - каждый метод несет одну ответственность


import requests, pandas

# метод получения данных объявлений по id
def getAdvertsData(advertsIDs):
    #делаем запрос в api
    requests.request('GET', '')
    #парсим ответ
    #возвращаем результат

    pass




# метод получения уникальных id пользоватеья из данных объявления
def getUsersIds(advertsData): pass

# метод получения данных пользовател
def getUsersData(usersIds): pass

# метод создающий финальную структуру
def getFinalDataFrame(advertsData,usersData): pass

def main():
    advertsData = getAdvertsData([18870423,29267386,26942404,30599151])

    # userIds = getUsers



main()
