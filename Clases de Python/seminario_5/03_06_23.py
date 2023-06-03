# n = int(input('Vvedite chislo N: '))
# def fib(n):
#     if n in[1, 2]:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
# print(fib(n))

# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1
"""
new = [1, 3, 5, 3, 4]

def new_arr(new_list):
    min_= min(new_list)
    max_= max(new_list)
    for i in range(len(new_list)):
        if new_list[i] == max_:
            new_list[i] = min_
    return new_list

print(new_arr(new))
"""
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)
# Input: 5
# Output: yes
"""
def simple_num(num):
    for i in range(2, num - 1):
        if num%i == 0:
            return 'No'
    return 'Yes'
    
print(simple_num(1))
"""
# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input:  2 -> 3 4
# Output: 4 3

def reverse_input(n):
    num = input('--> ')
    if n == 1:
        return num
    return reverse_input(n - 1) + ' ' + num
print(reverse_input(3))

