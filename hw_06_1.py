"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

import time


class TrafficLight:
    __color = 'RED'

    def running(self, color="RED", blink: int = 10):
        """
        Иммитирует работу светофора. Показывает какой цвет будет видеть наблюдатель с течением времени
        :param blink: количество переключений
        :param color: стартовый цвет
        :return:
        """
        self.__color = color.lower()
        time_dict = {"red": 7, "yellow": 2, "green": 5}
        light_tuple = ("red", "yellow", "green", "yellow")
        num = 0

        for en, el in enumerate(light_tuple, 1):
            if el == self.__color:
                num = en
        if num == 0:
            print("Цвет не входит в диапазон. Выход из программы")
            exit()
        i = 0
        res_time = 0
        while i < blink:
            time_start = time.time()
            print(f'На {res_time} секунде на светофоре будет цвет - {self.__color}')
            while (time.time() - time_start) < (time_dict[self.__color]):
                pass
            res_time += time_dict[self.__color]
            num += 1
            if num > 4:
                num = 1
            i += 1
            self.__color = light_tuple[num - 1]


li1 = TrafficLight()
li1.running("Green", 12)
print("Наблюдение завершено")