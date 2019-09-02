numb = int(input("Введите произвольное число от 0 до 10: "))

while not 0 < numb < 10:
    print("Число введено не верно!")
    numb = int(input("Введите произвольное число больше 0 и меньше 10: "))
else:
    multiply = numb * numb
    print("Результат от возведения в степень:", multiply, ".")