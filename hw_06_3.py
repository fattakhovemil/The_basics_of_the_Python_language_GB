"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""

class Worker:
    def __init__(self, name: str, surname: str, wage: float, bonus: float):
        self.name = name
        self.surname = surname
        self._income = {"wage": wage, "bonus": bonus}

    def get_full_name(self):
        print(f'Полное имя работника {self.name + " " + self.surname}')

    def get_total_income(self):
        print(f'Полный доход составит: {self._income["bonus"] + self._income["wage"]}')


class Position(Worker):
    def __init__(self, position: str, experience: float, name, surname, wage, bonus):
        super().__init__(name, surname, wage, bonus)
        self.position = position
        self.experience = experience


pos1 = Position("слесарь", 12.5, "Леша", "Иванов", 5000, 1333)
wor1 = Worker("Инокентий", "Петушнинский", 5000, 1500)
wor1.get_full_name()
wor1.get_total_income()
pos1.get_full_name()
pos1.get_total_income()