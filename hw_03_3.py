"""
3.Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""

def my_func (arg_1, arg_2, arg_3):
    try:
        array = [int(arg_1), int(arg_2), int(arg_3)]
    except ValueError as e:
        return 'Один из аргументов не является числом'
    return f'Сумма двух наибольших аргументов равна {sum(array) - min(array)}'

one = input('Введите аргумент 1 ')
two = input('Введите аргумент 2 ')
three = input('Введите аргумент 3 ')

print(my_func(one, two, three))