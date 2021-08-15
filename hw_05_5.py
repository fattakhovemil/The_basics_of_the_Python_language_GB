"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import os

filepath = os.path.join(os.getcwd(), 'exercise_5.txt')
print(filepath)
try:
    with open(filepath, 'w', encoding="UTF-8") as file_ob:
        my_str = input("Введите числовые значения через пробел\n")
        file_ob.write(my_str)

    with open(filepath, 'r', encoding="UTF-8") as file_ob:
        try:
            list_num = map(float, file_ob.read().split(sep=' '))
            print("Сумма чисел в файле = ", sum(list_num))
        except ValueError as er:
            print("Введено нечисловое значение", er)
except IOError as er:
    print("Ошибка ввода-вывода", er)