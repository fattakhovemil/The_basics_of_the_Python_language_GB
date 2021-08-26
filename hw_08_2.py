"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
"""

class ZeroError(Exception):

    def __init__(self, ):
        self.message = "Деление на 0 запрещено"


def division(a: float, b: float):
    try:
        if b == 0:
            raise ZeroError
        return a / b
    except ZeroError as er:
        print(er.message)


while True:
    x = input("Введите числовое значение делителя.'q' для выхода\n")
    if x.lower() == "q":
        break
    y = input("Введите числовое значение частного.'q' для выхода\n")
    if y.lower() == "q":
        break

    try:
        print(division(float(x), float(y)))
    except ValueError:
        print("Введены некорректные данные")