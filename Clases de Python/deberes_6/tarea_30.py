# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

n = int(input('Введите кол-во эл-ов арифметической прогрессии: '))
a = int(input('Введите с какого эл-та начать: '))
d = int(input('Введите шаг прогрессии: '))

new_arr = list()
for i in range(n):
    new_arr.append(a + ((i + 1) - 1) * d)

print(new_arr)
