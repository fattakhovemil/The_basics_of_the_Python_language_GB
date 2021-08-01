"""Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict."""

number_of_month = int(input("Enter number of month: "))

dict = {'Winter': [12, 1, 2], 'Spring': [3, 4, 5], 'Summer': [6, 7, 8], 'Autumn': [9, 10, 11]}
list = ['Winter', 'Spring', 'Summer', 'Autumn']
season_id = number_of_month // 3


if (season_id == 4) or (season_id < 1):
    print(list[0])
else:
    print(list[season_id])


for key, value in dict.items():
    if number_of_month in value:
        print(f"This is {key}")