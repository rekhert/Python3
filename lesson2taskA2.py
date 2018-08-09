print('\n Задания сложности A'
      '\n 2 Напишите программу которая будет форматировать введенне число' 
      '\n 1 в процентах 0,15542352  => 15.5%')

number = float(str(input('\n enter a number to be converted in %:')).replace(",", "."))

print('{:.2%}'.format(number))


print('\n Задания сложности A'
      '\n 2 Напишите программу которая будет форматировать введенне число'
      '\n 2 в валюте 3542352515,156467496846546 => 3,542,352,515.15 $')

number1 = float(str(input('\n enter a number to be converted in $ amount:')).replace(",", "."))

print('{:,}'.format(number1), "$")