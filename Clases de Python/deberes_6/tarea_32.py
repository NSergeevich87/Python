# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

def arr_random(size):
    new_arr = list()
    for i in range(size):
        new_arr.append(random.randint(1, 5))
    return new_arr

def find_indexes(arr, a, b):
    numbers_indexes = list()
    for i in range(len(arr)):
        if a <= arr[i] <= b:
            numbers_indexes.append(i)
    return numbers_indexes

size_arr = int(input('Введите кол-во элементов в массиве: '))
num_min = int(input('Введите диапазон чисел ОТ: '))
num_max = int(input('Введите диапазон чисел ДО: '))

new_arr = arr_random(size_arr)
result = find_indexes(new_arr, num_min, num_max)

print(new_arr)
print(f'Вот ИНДЕКСЫ элементов из заданного диапазона: {result}')



