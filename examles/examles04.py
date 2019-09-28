def print_sep(sep1, len1):
    return sep1 * len1


print(print_sep("*", 50))
print(print_sep("-", 100))

sep = print_sep("3", 15)
text = 'hello {} Func {} - {}'.format(sep, sep, sep)

print(text)


def hello(who, say='hello'):
    print(say, who)


hello('leo')


def hello_args(*args, say='hello'):  # тут на вход приходит кортеж
    print(say, args)


hello_args('leo', 'max', 'kelly', 'bring')


def hello_kwargs(**kwargs):  # тут на вход приходит словарь
    for k, w in kwargs.items():
        print(k, w)


hello_kwargs(name='leo', age=25, has_car=True)

print()


# функции в параметре
def some_f():
    return 10


result = some_f()
print(result)

a = some_f
print(a)
print(type(a))
print(a())

print()


# передача функций в параметрах
def f():
    print('sdfsfasfsdfgdfsgs')


def to(f_param):
    # параметром будет функция
    # поэтому в теле функции to мы ее вызовем
    f_param()


to(f)

# лямбды заменяют функции в параметрах foo(lambda number: number % 2 == 0) - будет передана функция в качестве аргумента
# которая будет искать четные числа в массиве number
