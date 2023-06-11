# Задача 38: 
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. 
# Ваша программа не должна быть линейной
# 5. Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

def write_contacts(filename):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write('\n' + str.lower(input(f'Введите через пробел: ФИО и номер телефона -> ')))
    return file

def read_contacts(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line)

def find_contacts(filename):
    find = str.lower(input('Введите данные для поиска: '))
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if find in line:
               print(line)

def edit_contacts(filename):
    words = str.lower(input('Введите, что будем менять -> '))
    with open(filename, 'r', encoding='utf-8') as file:
        old_data = file.read()
        new_data = old_data.replace(words, str.lower(input('Введите на что заменить -> ')))
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(new_data)

filename = r'Clases de Python\deberes_8\book.txt'
flag = True
while flag:
    ask = int(input('1 - для ввода, 2 - для вывода, 3 - для поиска, 4 - для редактирования или удаления \n'))
    if ask == 1:
        write_contacts(filename)
        answ = str.lower(input('Продолжаем? да/нет -> '))
        if answ == 'нет': flag = False
        else: continue
    elif ask == 2:
        read_contacts(filename)
        answ = str.lower(input('Продолжаем? да/нет -> '))
        if answ == 'нет': flag = False
        else: continue
    elif ask == 3:
        find_contacts(filename)
        answ = str.lower(input('Продолжаем? да/нет -> '))
        if answ == 'нет': flag = False
        else: continue
    elif ask == 4:
        edit_contacts(filename)
        answ = str.lower(input('Продолжаем? да/нет -> '))
        if answ == 'нет': flag = False
        else: continue
    else:
        print('Нет такой функции!')