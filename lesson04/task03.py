# Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
#
#     name - строка полученная от пользователя,
#     health = 100,
#     damage = 50.
# Поэкспериментируйте с значениями урона и жизней по желанию.
# ### Теперь надо создать функцию attack(person1, person2).
# Примечание: имена аргументов можете указать свои.
# ### Функция в качестве аргумента будет принимать атакующего и атакуемого.
# ### В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения.

person1 = input("Введите имя атакующего: ")
person2 = input("Введите имя атакуемого: ")
health = 100
damage = 50

dictionary1 = {person1: damage, person2: health}


# print(dictionary1)
# print(dictionary1.get(person2))

def attack(health_f, damage_f):
    dictionary1[person2] = health_f - damage_f


print(f'Персоны до атаки: {dictionary1}, т.е. здоровье = {dictionary1.get(person2)}')  # health = 100
attack(dictionary1.get(person2), dictionary1.get(person1))  # функция производит атаку  person1 на person2
print(f'Персоны после атаки: {dictionary1}, т.е. здоровье = {dictionary1.get(person2)}')  # health = 50
