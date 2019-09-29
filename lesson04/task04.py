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

dictionary2 = {person1: damage, person2: (health, armor)}


def armor_f(damage_f, armor_v):
    return damage_f / armor_v


def attack(health_f, armor_v, damage_f):
    result = armor_f(damage_f, armor_v)
    dictionary2[person2] = (
        health_f - result, dictionary2[person2][1])  # в этом месте функция обрабатывает кортеж словаря


print(f'Персоны до атаки: {dictionary2}, т.е. здоровье = {dictionary2[person2][0]}')  # health = 100
attack(dictionary2[person2][0], dictionary2[person2][1],
       dictionary2.get(person1))  # функция производит атаку  person1 на person2
print(f'Персоны после атаки: {dictionary2}, т.е. здоровье = {dictionary2[person2][0]}')  # health = 58.33333333333333
