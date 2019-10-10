import sys
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info

save_info('Старт')

command = sys.argv[1]

# print(sys.argv)

if command == 'list':
    get_list()
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
