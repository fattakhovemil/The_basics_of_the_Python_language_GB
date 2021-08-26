"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""

import datetime


class Date:
    month_dict = {"Январь": 1,
                  "Февраль": 2,
                  "Март": 3,
                  "Апрель": 4,
                  "Май": 5,
                  "Июнь": 6,
                  "Июль": 7,
                  "Август": 8,
                  "Сентябрь": 9,
                  "Октябрь": 10,
                  "Ноябрь": 11,
                  "Декабрь": 12,
                  }

    def __init__(self, date: str):
        self.__date = date

    @classmethod
    def transform(cls, date):
        date_list = date.split('-')
        # print(date_list)
        try:
            day = int(date_list[0])
            month = Date.month_dict[date_list[1].capitalize()]
            year = int(date_list[2])
            print(f'Преобразование прошло успешно. День - {day}, месяц - {month}, год - {year}')
            return year, month, day
        except ValueError as er:
            print("Дата введена не по шаблону (день, год). Выход из программы", er)
            return None
        except KeyError as er:
            print(f"Дата введена не по шаблону ({er}). Выход из программы", )
            return None

    @staticmethod
    def validation(year: int, month: int, day: int):
        date_to_val = None
        try:
            date_to_val = datetime.date(year, month, day)
        except ValueError as dat_err:
            print("Дата не может быть сформирована по внесенным данным (не входят в допустимы диапазон)", dat_err)
        return f'Дата корректна: {date_to_val.strftime("%d.%m.%Y")}' if date_to_val is not None else None


if __name__ == '__main__':
    # day1 = Date("22-Июль-2020")
    print(Date.transform("22-январь-1925"), "\n")
    print(Date.validation(1193, 1, 12) + "\n")
    print(Date.validation(*Date.transform("31-Август-1987")))