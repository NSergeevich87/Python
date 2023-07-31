SaveBook = r'NoteAppPython\SaveBook.txt'

def write_contacts(SaveBook):
    with open(SaveBook, 'a', encoding='utf-8') as file:
        file.write('\n' + str.lower(input(f'Введите через пробел: ФИО и номер телефона -> ')))
    return file

def read_contacts(SaveBook):
    with open(SaveBook, 'r', encoding='utf-8') as file:
        for line in file:
            print(line)

def find_contacts(SaveBook):
    find = str.lower(input('Введите данные для поиска: '))
    with open(SaveBook, 'r', encoding='utf-8') as file:
        for line in file:
            if find in line:
               print(line)

def edit_contacts(SaveBook):
    words = str.lower(input('Введите, что будем менять -> '))
    with open(SaveBook, 'r', encoding='utf-8') as file:
        old_data = file.read()
        new_data = old_data.replace(words, str.lower(input('Введите на что заменить -> ')))
    with open(SaveBook, 'w', encoding='utf-8') as file:
        file.write(new_data)
        

flag = True
while flag:
    ask = int(input(
        '1 - для ввода,' +  
        '2 - для вывода,' + 
        '3 - для поиска,' + 
        '4 - для редактирования или удаления \n'))
    if ask == 1:
        write_contacts(SaveBook)
        answ = str.lower(input('Продолжаем? да/нет -> '))
        if answ == 'нет': flag = False
        else: continue
    elif ask == 2:
        read_contacts(SaveBook)
        answ = str.lower(input('Продолжаем? да/нет -> '))
        if answ == 'нет': flag = False
        else: continue
    elif ask == 3:
        find_contacts(SaveBook)
        answ = str.lower(input('Продолжаем? да/нет -> '))
        if answ == 'нет': flag = False
        else: continue
    elif ask == 4:
        edit_contacts(SaveBook)
        answ = str.lower(input('Продолжаем? да/нет -> '))
        if answ == 'нет': flag = False
        else: continue
    else:
        print('Нет такой функции!')
        
