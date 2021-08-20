"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

class Car:
    def __init__(self, speed: float, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Driving has started. Car - {self.name}")

    def stop(self):
        print(f"Driving has stopped. Car - {self.name}")

    def turn(self, direct: str = "right" or "left"):
        print(f'Car {self.name} has turned {direct}')

    def show_speed(self):
        print(f'car speed = {self.speed} km per hour')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'{self.name} car speed = {self.speed} km per hour. {"!!!!Speeding!!!!" if self.speed > 40 else ""}')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)
        self.is_police = is_police

    def show_speed(self):
        print(f'{self.name} car speed = {self.speed} km per hour. {"!!!!Speeding!!!!" if self.speed > 60 else ""}')


car1 = PoliceCar(60, "Red", "UAZ")
car2 = PoliceCar(65, "White and Blue", "Ford")
car1.show_speed()
car2.show_speed()
print("-" * 100)
car3 = TownCar(39, "Red", "Lada")
car4 = TownCar(55, "White", "Opel")
car3.show_speed()
car4.show_speed()
print("-" * 100)
car5 = Car(99, "Black", "Subaru", False)
car5.show_speed()
print("-" * 100)
car5.turn("right")