"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов
сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""

class ComplexNum:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Комплексное число: {self.x}{"+" if self.y >= 0 else ""}{self.y}j'

    def __add__(self, other):
        return ComplexNum(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return ComplexNum(self.x * other.x - self.y * other.y, self.x * other.y + other.x * self.y)


if __name__ == '__main__':
    com_num1 = ComplexNum(3, 3)
    com_num2 = ComplexNum(7, -2)
    com_num3 = com_num1 + com_num2
    com_num4 = com_num1 * com_num2
    cn3 = complex(3 + 3j) + complex(7 - 2j)
    cn4 = complex(3 + 3j) * complex(7 - 2j)

    print(com_num1)
    print(com_num2)
    print(f"Результат сложения: {com_num3}. Проверка встроенной функции: {cn3}")
    print(f"Результат умножения: {com_num4}. Проверка встроенной функции: {cn4}")