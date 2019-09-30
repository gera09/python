# 1: Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py).
# В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой
# запущен данный код. Затем создайте вторую функцию удаляющую эти папки. Проверьте
# работу функций в этом же модуле.

import os


def mkdir(dir_project):
    for x in range(1, 10):
        new_path_ = f'{os.getcwd()}\\dir_{x}'  # реализация через переменные
        os.mkdir(new_path_)


def del_dir(del_dir):
    for i in range(1, 10):
        new_path = os.path.join(os.getcwd(), f'dir_{i}')  # реализация через join
        os.rmdir(new_path)


if __name__ == "__main__":
    print('Каталоги еще НЕ созданы!')
    print('Список каталогов и файлов папки проекта в текущий момент:')
mkdir(os.getcwd())

if __name__ == "__main__":
    print(os.listdir(os.getcwd()))

if __name__ == "__main__":
    print('Каталоги созданы!')

# печатаем все каталоги и файлы текущей папки проекта
if __name__ == "__main__":
    print('Список каталогов и файлов папки проекта в текущий момент:')
del_dir(os.getcwd())

if __name__ == "__main__":
    print(os.listdir(os.getcwd()))

if __name__ == "__main__":
    print('Каталоги удалены!')
