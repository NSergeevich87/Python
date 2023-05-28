# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()
"""
str_1 = 'a a a b c a a d c d d'.split()
letters = {}
result = ''
for i in range(len(str_1)):
    if str_1[i] not in letters.keys():
        letters[str_1[i]] = 1
        result += f'{str_1[i]} '
    else:
        result += f'{str_1[i]}_{letters[str_1[i]]} '
        letters[str_1[i]] += 1
print(result)

input = ('a a a b c a a d c d d').split()
out = {}
for i in input:
    if i in out:
        print(f'{i}_{out[i]}', end=' ')
    else:
        print(i, end=' ')
    out[i] = out.get(i, 0) + 1
"""
# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
# Input: 
# She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13
"""
str_ = "She sells sea shells on the sea shore The shells that she sells are sea shells 
        I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells".lower().split()
print(len(set(str_)))
"""
# Ваня и Петя поспорили, кто быстрее решит следующую задачу: 
# “Задана последовательность неотрицательных целых чисел. Требуется определить значение наибольшего элемента последовательности, 
# которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”. Однако 2  друга оказались не такими смышлеными. 
# Никто из ребят не смог до конца сделать это задание. Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. 
# За помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих слайдах

numbers = []
print('Начните вводить числа: ')
n = -1
max = 0

while n != 0:
    n = int(input())
    numbers.append(n)

for i in numbers:
    if i > max:
        max = i 

print(numbers)
print(max)