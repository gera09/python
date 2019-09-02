my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]

for y in my_list_2:
    # print('y', y)
    if my_list_1.count(y) > 0:
        for x in range(my_list_1.count(y)):
            my_list_1.remove(y)
        # print(my_list_1)

print(my_list_1)
