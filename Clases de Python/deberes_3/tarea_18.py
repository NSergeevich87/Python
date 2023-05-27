# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
#     5
#     1 2 3 4 5
#     6
#     -> 5

import random

print('Введите кол-во элементов в массиве.')
num = int(input())
arr = []

for i in range(num):
    # arr.append(int(input()))
    arr.append(random.randint(1, 10))

print('Введите число, чтобы определить самый близкий по величине элемент.')
x = int(input())
result = x
answer = arr[0]
for i in range(len(arr)):
    temp = x - arr[i]
    if temp < result and temp >= 0:
        result = x - arr[i]
        answer = arr[i]

print(arr)
print(f'Самый близкий по величине элемент = {answer}')