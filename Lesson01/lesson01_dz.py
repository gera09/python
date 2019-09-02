name = input("Введите имя: ")
surname = input("Введите фамилию: ")
age = int(input("Введите свой возраст: "))
weight = int(input("Введите свой вес: "))
status = str("")

if age < 30 and 50 < weight < 120:
    status = 'хорошее состояние'

elif 30 <= age < 40 and (weight <= 50 or weight >= 120):
    status = 'следует заняться собой'

elif age >= 40 and (weight <= 50 or weight >= 120):
    status = 'следует обратиться к врачу!'

elif 30 <= age < 40 and (weight >= 50 or weight <= 120):
    status = 'хорошее состояние'

else:
    print('Ошибка. Введены некорректные данные!')

print(str(name) + " " + str(surname) + " " + str(age) + " год " + "вес " + str(weight) + " - " + str(status))