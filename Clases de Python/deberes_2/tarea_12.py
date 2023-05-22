# Задача 12: 
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2 or 5 6 -> 2 3

numUno = int(input('Введите сумму задуманных чисел -> '))
numDos = int(input('Введите произведение задуманных чисел -> '))

for i in range(numUno):
    for j in range(numDos):
        if numUno == i + j and numDos == i * j:
            print(f'Вы загадали -> {i}, {j}')

# import math

# numUno = int(input('Введите сумму задуманных чисел -> '))
# numDos = int(input('Введите произведение задуманных чисел -> '))

# status = False
# while status == False:
#     x = int(input(f'Попробуйте догадаться чему равно первое число, если сумма задуманных чисел = {numUno}, а их произведение = {numDos} -> '))
#     y = int(input(f'А второе? -> '))
#     if x + y == numUno:
#         if x * y == numDos:
#             print(f'Отлично! Вы нашли числа: {x}, {y}')
#             status = True
#         else: 
#             test = input('Ответ не верен. Для продолжения нажмите любую клавишу или напишите - "ОТВЕТ" для вывода результата.')
#             if test != 'ОТВЕТ':
#                 status = False
#             else:
#                 answer = int(numUno * numUno - 4 * numDos)
#                 if answer < 0:
#                     print('Решений нет!')
#                 x = (numUno + math.sqrt(answer)) / 2
#                 y = (numUno - math.sqrt(answer)) / 2
#                 print(x, y)
#     else: 
#         test = input('Ответ не верен. Для продолжения нажмите любую клавишу или напишите - "ОТВЕТ" для вывода результата.')
#         if test != 'ОТВЕТ':
#             status = False
#         else:
#             answer = int(numUno * numUno - 4 * numDos)
#             if answer < 0:
#                 print('Решений нет!')
#             x = (numUno + math.sqrt(answer)) / 2
#             y = (numUno - math.sqrt(answer)) / 2
#             print(x, y)

# x = int(input())
# y = int(input())
# for i in range(x):
#     for j in range(y):
#         if x == i + j and y == i * j:
#             print(i, j)







