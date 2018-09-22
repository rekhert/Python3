#
# #1
# try:
#     10* (1/0)
# except Exception as e:
#     print("error")
#     print(e)
#
# #2
# try:
#     raise FileExistsError('file doesn\'t exist')
# except Exception as e:
#     print("error")
#     print(e)
#
# #3
# try:
#     raise FileExistsError('file doesn\'t exist')
#     10*(1/0)
#
#
#
# #4
# x = {'key':'value'}
#
# try:
#     y = x['key2']
# except KeyError as e:
#     print(e)
#     print('key not found')
#     y = None
# print(y)

#делать код отказоустойчивым, но не немым

#5
# errorCounter = 0
# try:
#
#     try:
#         raise AttributeError('error has occured')
#     except Exception as e:
#         print(e)
#         errorCounter += 1
#
#     try:
#         y = x['key2']
#     except KeyError as e:
#         print(e)
#         print('key not found')
#         y = None
#         errorCounter +=1
#     else:
#         print('key found')
#         print(y)
#
#     finally:
#         print('work anyway')
#
#
# except Exception as e:
#     errorCounter +=1
#     print("{}errors".format(errorCounter))
# print("program has finished with {} errors".format(errorCounter))



#6

dataSet = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",

}
keys =  [
    'key1',
    'key2',
    'key3',
    'key',
    'ke1',
    'key8',
    'key22'
    ]

collection = {}
for k in keys:
    try:
        collection[k] = dataSet[k]
    except KeyError as e:
        collection[k] = 'na'
        print('logging error {}'.format(e))
    else:
        print('key found')
    finally:
        print('iteration finished')

print(collection)

for k, v in collection.items():
    print(k, v)

#6
# написать модуль алгоритмов, в котором будет реализованы, ф
# ибоначи, решето эратосфена, сортировку пузырьком

#7 skipped

#8
#напишите функцию которая из dict бесопасно вытаскивает значение по ключу,
#в случае если значения нет то возвращает значение по умолчанию
#getVelueByKey(dict, key, default)



#8
# программа поиска данных по зарегистрированым пользователям
# база -- dict тел книга  -- имя, фамилия, возраст, телефон, ДР
# -- введите имя
# -- введите фамилии
# в dict в качестве ключа использовать кортежи tuples
# {(name,surname):}
# tuples as keys
#
# возможность искать толбко по имени, только по фамилии, только по тел, только по возрасту
# вывести список юзеров отформатированный

