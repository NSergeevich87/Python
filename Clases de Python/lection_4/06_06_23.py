# map принимает функцию и аргументы, которые впоследствии прогоняет через заданную функцию
# where
# filter
# zip функция на вход которой подаются списки, а на выходе выдаются кортежи из элементов этих списков
# enumerate функция на вход которой подается список, а на выходе получаем пронумерованный список
# import os
# os.chdir(path) - Смена текущей директории
# os.getcwd() - Текущая рабочая директория
# os.path.basename(path) - Базовое имя пути
# os.path.abspath(path) - Возвращает нормализованный абсолютный путь
# import shutil
# shutil.copyfile(src, dst) - копирует содержимое но не метаданные
# shutil.copy(src, dst) - копирукт содержимое
# shutil.rmtree(path) - удаляет директорию
"""
def f(x, b):
    return x * b
def g(x, b):
    return x + b

def new_fun(fun, x, b):
    print(fun(x, b))

calk1 = lambda a, b: a ** b # Лямбда функция позволяет сократить строчки кода

new_fun(lambda a, b: a ** b, 3, 4)
"""
# new_list = [1, 2, 3, 5, 8, 15, 23, 38]
# new_list2 = list()
# j = 0
# for i in new_list:
#     if i % 2 == 0:
#         new_list2.append((i, i**2))
# print(new_list2)
"""
def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

new_list = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, new_list)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x**2), res))
print(res)
"""
# list_1 = [x for x in range(1, 20)]
# print(list_1)
# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)
"""
data = '9 8 7 6 54 45 678'
print(data)
data = list(map(int, data.split()))
print(data)
"""
# data = [87, 6, 5, 3, 4, 5, 6, 7, 0, 87]
# new_data = list(filter(lambda x: x % 10 == 7, data)) # filter встроенная функция в python которая позволяет отобрать определенные элементы
# print(new_data)
"""
data = list(zip([1, 2, 3],['q','w','e'],['r','t','y']))
print(data)
name = ['nikita','ksyunya']
date = [1987, 1989]
base = list(zip(name, date))
print(base)
"""
# numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# set_numbers = list(enumerate(numbers))
# print(set_numbers)

colors = ['red', 'green', 'blue']
data = open('file.txt', 'a') # здесь указываем режим в котором будем работать
data.writelines(colors)
data.close()

with open('file.txt', 'w') as data:
    data.write('line_1\n')
    data.write('line_2\n')
print()

path = 'file.txt'
data = open('file.txt', 'r')
for line in data:
    print(line)
data.close()

