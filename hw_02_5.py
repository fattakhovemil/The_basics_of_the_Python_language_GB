"""Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен
разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2]."""

while True:
    new_element = int(input("Enter new element of rating: "))
    try:
        if new_element < 1:
            print("This is not natural number")
            continue
        break
    except (TypeError, ValueError) as error:
        print('Reread the condition')
    continue

my_list = [7, 5, 3, 3, 2]

for i, j in enumerate(my_list, -1):
    if my_list[i] >= new_element >= my_list[i+1]:
        my_list.insert(i+1, new_element)
        break

if min(my_list) > new_element:
    my_list.append(new_element)
if max(my_list) < new_element:
    my_list.insert(0, new_element)

print(my_list)