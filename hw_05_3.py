"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

import os

file = os.path.join(os.path.dirname(__file__), 'my_text.txt')
poor_list = []
salary_list = []

try:
    with open(file, 'r', encoding="UTF-8-sig") as file_ob:
        if not file_ob.readlines():
            print("Файл пустой. Завершение программы")
            exit()
        file_ob.seek(0)
        for line in file_ob:
            line_list = line.split()
            print(line_list)
            if len(line_list) != 2:
                print("Количество слов в строке не 2. Завершение программы")
                exit()
            try:
                line_list[1] = float(line_list[1])
                salary_list.append(line_list[1])
                if float(line_list[1]) < 20000:
                    poor_list.append(line_list[0])
            except ValueError as er:
                print("Неверный формат строк в файле. Завершение программы", er)
                exit()

except IOError or FileNotFoundError as er:
    print(f"Ошибка ввода вывода или файл не найден: {er}")
    exit()

print("Список сотрудников имеет оклад менее 20 тыс.:", poor_list)
print(f"Средняя зарплата {len(salary_list)} сотрудников: ",
      0 if len(salary_list) == 0 else sum(salary_list) / len(salary_list))