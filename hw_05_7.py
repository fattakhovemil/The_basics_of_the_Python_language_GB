"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json
import os

file = os.path.join(os.path.dirname(__file__), 'exercise_7.txt')

dict_firm = {}
dict_aver = {}

try:
    with open(file, 'r', encoding="UTF-8-sig") as file_ob:
        for line in file_ob:

            line_list = line.split()
            try:
                dict_firm[line_list[0]] = float(line_list[2]) - float(line_list[3])
                print(line_list)
            except ValueError or TypeError as er:
                print("Данные в файле не соотвутсвуют образцу")
                exit()
        n = 0
        result = 0
        for keys, values in dict_firm.items():
            if values > 0:
                n += 1
                result += values
        aver = 0
        if n > 0:
            aver = result / n
        else:
            print("Расчет среднего не проводился (согласно условию)")
        dict_aver['average_profit'] = aver
        list_to_json = [dict_firm, dict_aver]

except IOError or FileNotFoundError as er:
    print(f"Ошибка ввода вывода или файл не найден: {er}")
print(list_to_json)


try:
    filepath = os.path.join(os.path.dirname(__file__), 'exercise_7.json')
    with open(filepath, 'w', encoding="UTF-8-sig") as w_json:
        json.dump(list_to_json, w_json)
except IOError or FileNotFoundError as er:
    print(f"Ошибка ввода вывода или файл не найден: {er}")