"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

import os

file = os.path.join(os.path.dirname(__file__), 'exercise_6.txt')

dict_study = {}
try:
    with open(file, 'r', encoding="UTF-8-sig") as file_ob:
        for lines in file_ob:
            line = lines
            line = line.replace(' —', '')
            #  print(line)
            name = line[:line.find(':')]
            hours_list = []
            i = line.count('(')

            while i:
                try:
                    hours_list.append(float(line[line.find(' ') + 1:line.find('(')]))
                    line = line[line.find('(') + 1:]
                    i -= 1
                except ValueError or TypeError as er:
                    print("Содержание файла не соответвует установленному", hours_list)
                    break
            dict_study[name] = sum(hours_list)

except IOError or FileNotFoundError as er:
    print(f"Ошибка ввода вывода или файл не найден: {er}")
print(dict_study)
