# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
"""
list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
print(len(set(list_1)))

sp = [1, 1, 2, 0, -1, 3, 4, 4]
sl = {}
for el in sp:
    sl[el] = sl.get(el, 0) + 1
    # if el not in sl:
    #     sl[el] = 1
    # else:
    #     sl[el] += 1
print(sl)
"""
# Задача №19. Общее обсуждение
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
"""
list_1 = [1, 2, 3, 4, 5]
k = 3
list_2 = list_1[k:] + list_1[0:k]
print(list_2)
"""
# Задача №21. Общее обсуждение
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005 "}, {"V": "S009"}, {"VIII": "S007"}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""
data = dict()
data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
num = set()
for d in data:
    for value in d.values():
        num.add(value)

print(num)

sl = dict()
sl = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
print(sl)
sl3= set()
sl2 = []
for element in sl:
    sl2.append(list(element.values()))
    sl3.add(*element.values())
print (sl3)
"""
# Задача N23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
"""
lst = [0, -1, 5, 2, 3]
count = 0
for i in range(len(lst)-1):
    if lst[i] < lst[i + 1]:
        count += 1
print(count)
"""
import random
sp = [random.randint(1, 100) for i in range(10)]
print(sp)
