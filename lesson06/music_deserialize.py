# Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle, прочитать из них
# информацию. И получить объект: словарь из предыдущего задания.

import pickle
import json

with open(f'group.pickle', 'rb') as f:
    my_favourite_group_new = pickle.load(f)

print("Вернем словарь из pickle проверим его тип:")
print(my_favourite_group_new)
print(type(my_favourite_group_new))

with open('group.json', 'r', encoding='utf-8') as f:
    my_favourite_group_new = json.load(f)

print("Вернем словарь из json проверим его тип:")
print(my_favourite_group_new)
print(type(my_favourite_group_new))
