"""
1.Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""

def divide(x, y):
    try:
        result = int(x) / int(y)
    except ZeroDivisionError as e:
        return 'Попытка делить на 0'
    return f'Результат деления {x} на {y} равен {result:.2f}'

numerator = input("Введите числитель ")
denominator = input("Введите знаменатель ")


print(f'{divide(numerator, denominator)}')