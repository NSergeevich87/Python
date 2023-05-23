# СПИСКИ!
list_1 = []
list_1 = list()
list_1 = [1, 2, 5, 8]
print(len(list_1))
print(list_1[0])

# append добавляет элемент в конец списка 
list_1.append(8)
list_2 = []
for i in range(5):
    list_2.append(i)
    print(list_2)

# pop удаляет последний элемент из списка
list_3 = [12, 7, -1, 21, 0]
print(list_3.pop())
a = list_3.pop(1)
print(a)
print(list_3)

# insert(позиция, значение) добавить элемент в определенное место
list_4 = [12, 7, -1, 21, 0]
print(list_4.insert(1, 9))
print(list_4)

# в списках работают срезы
print(list_4[len(list_4) - 2:])

# КОРТЕЖ! - это неизменяемый список!
t = (1, 2, 4,)
print(type(t))
v = [1, 8, 9]
print(type(v))
v = tuple(v)
print(type(v))
x, y, z = v       # РАСПАКОВКА КОРТЕЖА. ПРИСВОЕНИЕ ПЕРЕМЕННЫМ ПОСЛЕДОВАТЕЛЬНО ЧИСЕЛ ИЗ КОРТЕЖА
print(x, y, z) 

# СЛОВАРЬ!
d = {}
d = dict()
d['q'] = 'qwerty'
d['w'] = 'war'
print(d['w'])

# Удалить элемент в словаре. del + имя словаря
del d['w']

# Вывод элементов словаря.
d['f'] = 'fuck'
d['p'] = 'piggy'
for item in d:
    print(item, d[item])

# d.items() -   СОЗДАЕТ КОРТЕЖИ В СЛОВАРЕ!
print(d.items())
for (i, j) in d.items():
    print(i, j)

# МНОЖЕСТВА - могут быть только уникальные значения!
colors = {'red', 'green', 'blue'}
# добавить элемент в множество!
colors.add('grey')
print(colors)
# удалить элемент в множестве!
colors.remove('grey')
print(colors)
# .discard проверить нахождение элемента в множестве
colors.discard('grey')
# .clear очистить множество
colors.clear()
print(colors)

# ОПЕРАЦИИ СО МНОЖЕСТВАМИ
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # в С копируется множество А
u = a.union(b) # добавляет в U все уникальные элементы из множеств A и B
i = a.intersection(b) # добавит в i тольео те элементы которые присутствуют одновременно во множествах А и В
dl = a.difference(b) # вычитает из множества А повторные элементы из множества В
dr = b.difference(a) # {13, 21} вычитает из множ. В элем. которые присутвтвуют в А
q = a.union(b).difference(a.intersection(b))

# замороженное множество
a = {1, 8, 6}
b = frozenset(a) # работает как обычное множество, но мы его НЕ можем менять

# создать список из чисел от 1 до 100
new_list = []
for i in range(1, 101):
    new_list.append(i)
print(new_list)

new_list_2 = [(i, i) for i in range(1, 101) if i % 2 == 0]
print(new_list_2)


