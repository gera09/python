# 1. В консольный файловый менеджер добавить проверку ввода пользователя для всех функции с параметрами
# (на уроке разбирали на примере одной функции).
# 2. Добавить возможность изменения текущей рабочей директории.
# 3. Добавить возможность развлечения в процессе работы с менеджером. Для этого добавить в менеджер запуск одной
# из игр: “угадай число” или “угадай число (наоборот)”.

import os
import sys
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info

save_info('Старт')

# поиграем?
while True:
    msg = input('Хотите погирать? (y/n)')
    if msg == 'y':
        import gameHomework

        break
    elif msg == 'n':
        print('Хорошо, в другой раз!')
        break
    else:
        print('Вы ввели некорректное значение. Введите "y" или "n".')
        continue

while True:
    msg = input('Будете менять текущую рабочую директорию? (y/n)')
    if msg == 'y':
        work_dir = input('Введите директорию: ')
        if os.path.isdir(work_dir):
            os.chdir(work_dir)  # меняем директорию по умолчанию
            break
        else:
            print('Указанная директория не существует!')
            continue
    elif msg == 'n':
        break
    else:
        print('Вы ввели некорректное значение. Введите "y" или "n".')
        continue

command = sys.argv[1]

if command == 'list':
    try:
        folders_only = sys.argv[2]
    except IndexError:
        get_list()  # покажет только папки
    else:
        print(folders_only)
        if folders_only == '0' or folders_only == 'False' or folders_only == 'false' or folders_only == ' ':
            get_list()
        else:
            get_list(True)  # при наличие аргумента покажет и файлы и папки
elif command == 'create_file':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсуствует название файла')
    else:
        create_file(name)
elif command == 'create_folder':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсуствует название директории')
    else:
        create_folder(name)
elif command == 'delete':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсуствует название директории или файла')
    else:
        delete_file(name)
elif command == 'copy':
    try:
        name = sys.argv[2]
        new_name = sys.argv[3]
    except IndexError:
        print('Введите имя копируемой/-ого и новой/-го директории или файла')
    else:
        copy_file(name, new_name)
elif command == 'help':
    print('list - список файлов')
    print('create_file - создание файла')
    print('create_folder - создание папки')
    print('delete - удаление файла или папки')
    print('copy - копирование файла или папки')

save_info('Конец')
