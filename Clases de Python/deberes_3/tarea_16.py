# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
#     5
#     1 2 3 4 5
#     3
#     -> 1

print('Введите кол-во элементов в массиве.')
num_of_arr = int(input())
arr = []

print('Начните вводить числа.')
for i in range(num_of_arr):
    arr.append(int(input()))

print('Введите число, чтобы определить сколько раз оно встречается.')
x = int(input())
count = 0
for i in range(len(arr)):
    if arr[i] == x:
        count += 1

print(f'Введенное число встречается {count} раз')