# Решить с помощью генераторов списка.
#
# 1: Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
#     Примечание: Списки фруктов создайте вручную в начале файла.


fruits_1 = ['apple', 'strawberry', 'grape', 'plum', 'pineapple']
fruits_2 = ['apple', 'lemon', 'grape', 'cherry', 'pineapple']

result = [x for x in fruits_1 if x in fruits_2]
print(result)
