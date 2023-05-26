# Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных

def print_phone_book(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            print(*line.split(';'), end='')


def input_phone_book(file_name: str):
    with open(file_name, 'r+', encoding='utf-8') as data:
        record_id = 0
        for line in data:
            if line != '':
                record_id = line.split(';', 1)[0]
        print('Введите фамилию, имя, номер телефона через пробел')
        line = f'{int(record_id) + 1};' + ';'.join(input().split()[:4]) + ';\n'
        data.write(line)

def seach_phone_book(file_name: str, char, condition):
    if condition != 'q':
        printed = False
        with open(file_name, 'r', encoding='utf-8') as data:
            for line in data:
                if condition == line.split(';')[int(char)]:
                    print(*line.split(';'))
                    printed = True
        if not printed:
            print("Не найдено")
        return printed

def find_char():
    print('Выберите :')
    print('0 - id, 1 - фамилия, 2 - имя, 3 - номер, q - выйти')
    char = input()
    while char not in ('0', '1', '2', '3', 'q'):
        print('Введены неверные данные')
        print('Выберите характеристику:')
        print('0 - id, 1 - фамилия, 2 - имя, 3 номер, q - выйти')
        char = input()
    if char != 'q':
        inp = input('Введите значение\n')
        return char, inp
    else:
        return 'q', 'q'

def change_phone_book(file_name: str):
    book_id = check_id_record(file_name, 'изменить')
    if book_id != 'q':
        replaced_line = f'{int(book_id)};' + ';'.join(input('Введите фамилию, имя, номер телефона через пробел\n').split()[:4]) + ';\n'
        replace_record(file_name, book_id, replaced_line)

def check_id_record(file_name: str, text: str):
    decision = input(f'Вы знаете id записи которую хотите {text}? 1 - да, 2 - нет, q - выйти\n')
    while decision not in ('1', 'q'):
        if decision != '2':
            print('Введены неверные данные')
        else:
            seach_phone_book(path, *find_char())
        decision = input(f'Вы знаете id записи которую хотите {text}? 1 - да, 2 - нет, q - выйти\n')
    if decision == '1':
        record_id = input('Введите id, q - выйти\n')
        return record_id
    return decision

def replace_record(file_name: str, record_id, replaced_line: str):
    replaced = ''
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            replaced += line
            if record_id == line.split(';', 1)[0]:
                replaced = replaced.replace(line, replaced_line)
    with open(file_name, 'w', encoding='utf-8') as data:
        data.write(replaced)

def delete_phone_book(file_name: str):
    record_id = check_id_record(file_name, 'удалить')
    if record_id != 'q':
        replace_record(file_name, record_id, '')


path = 'phone_book.txt'
file = open(path, 'r')
file.close()

actions = {'1': 'печать справочника',
           '2': 'внесение записи в справочник',
           '3': 'поиск',
           '4': 'изменение данных',
           '5': 'удаление данных',
           '6': 'выход'}

action = None
while action != '6':
    print('Какое действие хотите совершить?', *[f'{i} - {actions[i]}' for i in actions])
    action = input()
    if action not in actions:
        print('Введены неверные данные')
    if action != '6':
        if action == '1':
            print_phone_book(path)
        elif action == '2':
            input_phone_book(path)
        elif action == '3':
            seach_phone_book(path, *find_char())
        elif action == '4':
            change_phone_book(path)
        elif action == '5':
            delete_phone_book(path)