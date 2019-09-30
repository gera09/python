# Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент.
# Если список пустой функция должна вернуть None. Проверьте работу функций в этом же модуле.
#     Примечание: Список для проверки введите вручную. Или возьмите этот: [1, 2, 3, 4]

from random import choice


def random_funk(list_in):
    if len(list1) > 0:
        return choice(list_in)
    else:
        return None


list1 = []
if __name__ == "__main__":
    print(f'Список пустой: {random_funk(list1)}')
list1 = [0, 4]
if __name__ == "__main__":
    print(f'Список НЕ пустой, случайное число: {random_funk(list1)}')
