my_list_1 = [2, 2, 5, 12, 8, 2, 12]
my_list_2 = []

# my_list_1 = [int(i) for i in input().split()] # пользовательский ввод через пробел

for i in my_list_1:
    if my_list_1.count(i) == 1:
        my_list_2.append(i)

print(my_list_2)
