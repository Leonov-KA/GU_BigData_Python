"""
1) Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
(зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный,
желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        import time
        while i < 3:
            print(TrafficLight.__color[i])
            if i == 0:
                time.sleep(7)
            elif i == 1:
                time.sleep(2)
            elif i == 2:
                time.sleep(5)
            i += 1


a = TrafficLight()
a.running()


"""
2)Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной
в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""
print("\n\n\n")


class Road:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width
        self.__weight = 25
        self.__height = 5

    def asphalt_mass(self):
        asphalt_mass = int(self.__length * self.__width * self.__weight * self.__height / 1000)
        print(f'Для участка дороги длинной {self.__length}м и шириной {self.__width}м, '
              f'неободимо {asphalt_mass} тонн асфальта')


b = Road(5000, 20)
b.asphalt_mass()


"""
3) Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения 
атрибутов, вызвать методы экземпляров).
"""
print("\n\n\n")


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = str(name)
        self.surname = str(surname)
        self.position = str(position)
        self.__income = {"wage": float(wage), "bonus": float(bonus)}
        self._auxiliary = self.__income


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._auxiliary["wage"] + self._auxiliary["bonus"]


c = Position("Иван", "Иванов", "Водитель", '50000', '5000')
print(c.get_full_name(), c.get_total_income())


"""
4) Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""
print("\n\n\n")


class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = int(speed)
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} поехала,'

    def turn(self, turn):
        return f'{self.name} повернула {turn},'

    def show_speed(self):
        return f'её скорость: {self.speed},'

    def stop(self):
        return f'{self.name} остановилась.'


class TownCar(Car):

    def description(self):
        return '\nГородской автомобиль:\n'

    def show_speed(self):
        if self.speed > 60:
            exceeding = self.speed - 60
            return f'Внимание! Cкорость привышена на {exceeding}'


class SportCar(Car):
    def description(self):
        return '\nСпортивная тачка:\n'


class WorkCar(Car):

    def description(self):
        return '\nРабочая лошадка:\n'

    def show_speed(self):
        if self.speed > 40:
            exceeding = self.speed - 40
            return f'Внимание! Cкорость привышена на {exceeding}'


class PoliceCar(Car):
    def description(self):
        return '\nАтас, Копы:\n'


town = TownCar('Lada', 70, 'белый', False)
print(town.description(), town.go(), town.show_speed(), town.turn('в право'), town.turn('right'), town.stop())

sport = SportCar('Ferrari', 170, 'жёлтый', False)
print(sport.description(), sport.go(), sport.show_speed(), sport.turn('в право'), sport.stop())

work = WorkCar('KAMAZ', 30, 'серый', False)
print(work.description(), work.go(), work.show_speed(), work.turn('в лево'), work.stop())

police = PoliceCar('Kia', 100, 'синий', True)
print(police.description(), police.go(), police.show_speed(), police.turn('в лево'), police.stop())



"""
5) Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный 
метод для каждого экземпляра.
"""
print("\n\n\n")


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


pen = Pen('ручкой')
print(pen.draw())
pencil = Pencil('карандашем')
print(pencil.draw())
handle = Handle('маркером')
print(handle.draw())