"""
5.Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить
ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и
после этого завершить программу.
"""

def numberSum(numbers, totalSum):
    try:
        numbers = [int(number) for number in numbers.split()]
        totalSum += sum(numbers)
        return totalSum, True
    except ValueError as e:
        numbers = [int(number) for number in numbers.split() if number.isdigit()]
        totalSum += sum(numbers)
        return totalSum, False

totalSum = 0
proceed = True

while proceed:
    text = input('Введите строку чисел, разделенных пробелом, и нажмите Enter ')
    totalSum, proceed =numberSum(text, totalSum)
    print(totalSum)