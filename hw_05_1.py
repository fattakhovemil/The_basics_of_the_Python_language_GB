"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

import os

filepath = os.path.join(os.getcwd(), 'my_text.txt')
print(filepath)
with open(filepath, 'w', encoding="UTF-8") as file_ob:
    while True:
        try:
            my_str = input("Введите текст для записи в файл или пустую сткроку для завершения\n")
            if my_str == '':
                break
            file_ob.write(f'{my_str}\n')
        except IOError:
            print("Произошла ошибка ввода-вывода!")