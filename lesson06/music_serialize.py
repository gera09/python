# Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы, например:
# my_favourite_group = {
# 'name': 'Г.М.О.',
# 'tracks': ['Последний месяц осени', 'Шапито'],
# 'Albums': [{'name': 'Делать панк-рок','year': 2016},
# {'name': 'Шапито','year': 2014}]}
#
# С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
# Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.

import pickle
import json

my_favourite_group = {'name': 'Г.М.О.', 'tracks': ['Последний месяц осени', 'Шапито'],
                      'Albums': [{'name': 'Делать панк-рок', 'year': 2016}, {'name': 'Шапито', 'year': 2014}]}

print(f'Тип объекта: {type(my_favourite_group)}')

print('Используем pickle:')
print(pickle.dumps(my_favourite_group))

with open('group.pickle', 'wb') as f:
    pickle.dump(my_favourite_group, f)
print("Объект записан в файл group.pickle")


print()
print('Используем json:')
print(json.dumps(my_favourite_group, ensure_ascii=False))
print(f'Тип приведенного объекта json: {type(json.dumps(my_favourite_group, ensure_ascii=False))}')

with open('group.json', 'w', encoding='utf-8') as f:
    json.dump(my_favourite_group, f, ensure_ascii=False, indent=4)  # Решил украсить запись в файл)
print("Объект записан в файл group.json")
