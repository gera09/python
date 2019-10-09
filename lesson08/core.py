import os
import shutil
import datetime


#  функция для создания файла
def create_file(name, text=None):
    with open(name, 'w', encoding='Utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже есть')


def get_list(folders_only=False):
    rezult = os.listdir()
    if folders_only:
        rezult = [f for f in rezult if os.path.isdir(f)]
    print(rezult)


def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Такая папка уже есть')
    else:
        shutil.copy(name, new_name)


def save_info(massage):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {massage}'
    with open('log.txt', 'a', encoding='Utf-8') as f:
        f.write(result + '\n')


if __name__ == '__main__':
    # create_file('text.dat')
    # create_file('text.dat', 'some text')
    # create_folder('new_f')
    # create_folder('new_f1')
    get_list(work_dir1='C:\Projects\python')
    get_list(True)
    get_list()
    # delete_file('new_f1')
    # delete_file('text.dat')
    # copy_file('new_f', 'new_2')
    # create_file('text.dat')
    # copy_file('text.dat','text2.dat')
    # save_info('asd')
