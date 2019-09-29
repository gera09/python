# 4: Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр -
# # armor = 1.2 (величина брони персонажа)
# # Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# # Следовательно, у вас должно быть 2 функции:
# #
# #     Наносит урон. Это улучшенная версия функции из задачи 3.
# #
# #     Вычисляет урон по отношению к броне.
# #
# #     Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона
# #     и вычитания его из здоровья персонажа.

person1 = input("Введите имя атакующего: ")
person2 = input("Введите имя атакуемого: ")
health = 100
damage = 50
armor = 1.2

dictionary1 = {person1: damage, person2: health}


# print(dictionary1)
# print(dictionary1.get(person2))

def armor_f(damage1, armor1):
    return damage1 / armor1


def attack(dictionary2):
    result = armor_f(damage, armor)
    dictionary2[person2] = dictionary2.get(person2) - result


print(f'Персоны до атаки: {dictionary1}')  # health = 100
attack(dictionary1)  # функция производит атаку  person1 на person2
print(f'Персоны после атаки: {dictionary1}')  # health = 50
