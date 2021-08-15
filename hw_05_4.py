"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

import os
file = os.path.join(os.path.dirname(__file__), 'my_text.txt')
new_file = os.path.join(os.path.dirname(__file__), 'new_text.txt')
ru_en_dict = {'One': 'Один', 'Two': "Два", "Three": "Три", "Four": "Четыре"}

try:
    with open(file, 'r', encoding="UTF-8-sig") as r_file, open(new_file, 'a', encoding="UTF-8-sig") as w_file:
        for line in r_file:
            rw_list = line.split()
            rw_list[0] = ru_en_dict[rw_list[0]]
            line_to_write = ' '.join(rw_list)
            w_file.write(line_to_write + '\n')
except IOError or FileNotFoundError as er:
    print(f"Ошибка ввода вывода или файл не найден: {er}")