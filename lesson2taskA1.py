
print('\n Задания сложности A'
      '\n 1 Напишите программу которая попросит ввести ваше имя, фамилию,' 
      '\n и выведит приветствие на основе введенных данных.'
      '\n + очищает ввод от лишних пробелов и левых символов '
      '\n К примеру ввел - Игорь Елисеев, \n вывод'
      '\n \'Добрый день Игорь Елисеев, рады приветствовать вас!\'')

name = input('\n Введите Ваше имя:')
surname = input('\n Введите Вашу фамилию:')

print("Добро пожаловать,",name.strip(' ,!,@,#,$,%'),surname.strip(' ,!,@,#,$,%'))







