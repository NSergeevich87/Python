# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

# base = dict()

# n = r'Clases de Python\seminario_8\book.txt'

# with open(n) as file:
#     for line in file:
#         # surname, name, patronymic, phone = line.strip().split(',')
#         # contact = {
#         #         'name': name,
#         #         'surname': surname,
#         #         'patronymic': patronymic,
#         #         'phone': phone
#         #     }
#         key, value1, value2, value3 = line.strip().split()
#         base[key] = key.split()

# print(base)

def write_contacts(filename):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write('\n' + input(f'Введите имя фамилию и отчество и номер телефона: '))
    return file

def read_contacts(filename):
    contacts = []
    with open(filename, 'r') as file:
        for line in file:
            
            name, surname, patronymic, phone = line.strip().split(',')
            contact = {
                'name': name,
                'surname': surname,
                'patronymic': patronymic,
                'phone': phone
            }
            print(name, surname, patronymic, phone)
            contacts.append(contact)
    return contacts

# def indiv_contacts(filename):
#     contacts = []
#     a = input('Введите характеристику для поиска: ')
#     with open(filename, 'r') as file:
#         for line in file:
#             name, surname, patronymic, phone = line.strip().split(',')
#             contact = {
#                 'name': name,
#                 'surname': surname,
#                 'patronymic': patronymic,
#                 'phone': phone
#             }
#             contacts.append(contact)

filename = r'Clases de Python\seminario_8\book.txt'
a = int(input('1 - для ввода, 2 - для вывода \n'))
if a == 1:
    add_contact = write_contacts(filename)
elif a == 2:
    contact = read_contacts(filename)
    # print(f'{contact}')
else:
    print('Нет такой функции!')

