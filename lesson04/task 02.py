"""
2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.
"""
arr1 = []
for i in range(3):
    number = int(input(f"Введите число № {i+1}: "))
    arr1.append(number)


def max_arr(arr1):
    return max(arr1)

#print(arr1)
print(max_arr(arr1))
