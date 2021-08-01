"""Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input()."""

list_of_numbers = list(input('Enter your list: ').split(" "))
"""if len(list_of_numbers) % 2 == 0:
    for number, element in enumerate(list_of_numbers):
        if number % 2 == 0:
            list_of_numbers[number], list_of_numbers[number+1] = list_of_numbers[number+1], list_of_numbers[number]

else:
    for number, element in enumerate(list_of_numbers[:-1]):
        if number % 2 == 0:
            list_of_numbers[number], list_of_numbers[number+1] = list_of_numbers[number+1], list_of_numbers[number]

print(list_of_numbers)"""

# альтернативный вариант

i = 0
while i < len(list_of_numbers) - 1:
    list_of_numbers[i], list_of_numbers[i + 1] = list_of_numbers[i + 1], list_of_numbers[i]
    i += 2
print(list_of_numbers)