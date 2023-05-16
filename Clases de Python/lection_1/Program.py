"""
n = None 
print(type(n)) # понять тип переменной
print('fd\'ds') # \' отобразить еще одну ковычку или ""
"""
# print() комментировать сразу несколько строк ctrl + k + c
# print()
# print()
# print() раскомментировать ctrl + k + u
# ИНТЕРПОЛЯЦИЯ - получение сложной строки из нескольких простых
"""
a = 5
b = 5.89
c = 'hello'
print(a,'-', b,'-', c)
print(f"{a} - {b} - {c}")
print("{} - {} - {}".format(a, b, c))
"""

# TAB - это удобный отступ в 4 пробела

print('Введите первое число: ')
b = float(input())
a = float(input("Введите еще чило: "))
print(round(a * b, 3))      

# iter **= 5 Возводит в 5ю степерь - это аналог i++ c#

r = range(20, 101, 20)
for i in r:
    print (i)

c = 'Nikita Nikiforov'
for i in c:
    print(i)

line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print (line)

text = "moROZ Y solncE dEn CHudesniy,!"
print(len(text))
print('solncE' in text)
print(text.lower())
print(text.upper())
print(text.replace('solncE', 'солнце!'))
print(text[0:len(text):2]) # выводит с первого элемента , до конца и с шагом 2 или [::2]

      





