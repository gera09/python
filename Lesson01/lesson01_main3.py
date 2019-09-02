name = input("Введите имя: ")
surname = input("Введите фамилию: ")

age = int(input("Введите возраст: "))
while age <= 0 or age >= 150:
    print("Введен неверный возраст!")
    age = int(input("Введите возраст: "))
else:

    weight = int(input("Введите вес: "))
while weight <= 0 or weight >= 500:
    print("Введен неверный вес!")
    weight = int(input("Введите вес: "))
else:

    if (age <= 30) and (50 <= weight <= 120):
        print(name, surname, age, "год", weight, "кг - хорошее состояние")
    elif (30 < age <= 40) and (weight < 50 or weight > 120):
        print(name, surname, age, "год", weight, "кг - следует заняться собой")
    elif (age > 40) and (weight < 50 or weight > 120):
        print(name, surname, age, "год", weight, "кг - следует обратится к врачу!")
    else:
        print(name, surname, age, "год", weight, "кг - диагноз не установлен!")

"""
Пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
Пациенту требуется заняться собой, если ему более 30 и вес меньше 50 или больше 120 кг
Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
"""
