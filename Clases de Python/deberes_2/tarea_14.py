# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1, 2, 4, 8

number = int(input('Введите число: '))
counter = 0
answer = 1

while answer < number:
    print(answer)
    answer *= 2

# while 2 ** counter <= number:
#     print(2 ** counter)
#     counter += 1


