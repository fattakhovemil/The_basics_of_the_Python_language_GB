"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""

from abc import ABC, abstractmethod
from validation import valid_amount, valid_price


class Departments(ABC):

    def __init__(self):
        """
        Создает объеты предприятия
        """
        self.__city = "Moscow"
        self.__organization = "Gazprom"


class OfficeEq(ABC):
    def __init__(self):
        """
        Создание оргтихники
        """
        self.__manufacturer = "China"
        self.__voltage = 220

    @abstractmethod
    def __str__(self):
        pass


class Printers(OfficeEq):
    def __init__(self, name: str, amount: int, price: float, form: str):
        super().__init__()
        self.__name = name
        self.__price = price
        self.__amount = amount
        self.__form = form

        self.__amount = valid_amount(self.__amount)  # вадидация при создании. функция имортирована
        self.__price = valid_price(self.__price)

        self.__total_price = self.__amount * self.__price

    @property
    def equipment_list(self):
        return ["Принтеры", self.__name, self.__amount]

    def __str__(self):
        return f'Принтеры марки "{self.__name}" в кол-ве {self.__amount} шт.' \
               f' Цена {self.__price :.2f} y.е/шт. Total price: {self.__total_price} y.e.'


class Scanners(OfficeEq):
    def __init__(self, name: str, amount: int, price: float, resolution: int):
        super().__init__()
        self.__price = price
        self.__amount = amount
        self.__name = name
        self.__resolution = resolution

        self.__amount = valid_amount(self.__amount)  # вадидация при создании функции внешнего файла
        self.__price = valid_price(self.__price)

        self.__total_price = self.__amount * self.__price

    @property
    def equipment_list(self):
        return ["Сканнеры", self.__name, self.__amount]

    def __str__(self):
        return f'Сканнеры марки "{self.__name}" в кол-ве {self.__amount} шт.' \
               f' Цена {self.__price :.2f} y.е/шт. Total price: {self.__total_price} y.e.'


class Storage(Departments):
    def __init__(self, name):
        super().__init__()
        self.equipment_list = []
        self.name = name

    def __str__(self):
        return f'Текщее количество оборудования на складе:\n{self.equipment_list}'

    def add_equip(self, param: list):
        """
        Фугкция добавления оборудования на склад
        :param param:
        :return:
        """
        if not self.equipment_list:
            self.equipment_list.append(param)
        else:
            fl = 0
            for el in self.equipment_list:
                if el[0] == param[0] and el[1] == param[1]:
                    el[2] = el[2] + param[2]
                    fl = 1
            if fl == 0:
                self.equipment_list.append(param)
        return self.equipment_list


class Office(Departments):
    def __init__(self, name):
        super().__init__()
        self.equipment_list = []
        self.name = name

    def __str__(self):
        return f'Текщее количество оборудования офисе "{self.name}":\n{self.equipment_list}'

    def equip_to_give(self, name: str, model: str, amount: int):
        """
        Функция передачи оборудования со склада
        :param name:
        :param model:
        :param amount:
        :return:
        """
        if not storage1.equipment_list:
            print("На сладе не обнаружено товаров")
        else:
            fl = 0
            for el in storage1.equipment_list:
                if el[0] == name and el[1] == model:
                    fl = 1
                    if el[2] > amount:
                        el[2] = el[2] - amount
                        list_to_add = [name, model, amount]
                        self.equipment_list.append(list_to_add)
                        print(f"Со склада передано {amount} единиц оборудования серии '{name}-{model}'")
                    else:
                        print(f"операция не может быть проведена. На сладе меньше {amount}"
                              f" единиц запрашиваемого оборудования")
            if fl == 0:
                print("На складе нет указанного оборудования")
        return self.equipment_list


if __name__ == "__main__":

    printer1 = Printers("Xerox", "s", 456, "A4")  # для валидации вводимых данных
    printer2 = Printers("LaserJet", 8, 45, "A3")
    scan1 = Scanners("HP", 4, 321, 600)
    scan2 = Scanners("HP", 5, 321, 1200)

    storage1 = Storage("Склад 1")  # загрузка товара на склад
    for eq in [printer1, printer2, scan1, scan2]:
        storage1.add_equip(eq.equipment_list)
    print(storage1, '\n')

    office = Office("Унылая конторка")
    office.equip_to_give("Сканнеры", "HP", 4)  # передача части товара
    print(storage1, '\n')
    print(office, '\n')