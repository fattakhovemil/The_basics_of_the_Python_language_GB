"""Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе."""

list_of_types = [3, 3.14, 'string', False, {1, 2, 3}, (4, 5, 6), None, complex(5, 6)]
for i in list_of_types:
    print(f"{i} is {type(i)}")