class Vehicle:
    COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return self.__model

    def get_horsepower(self):
        return self.__engine_power

    def get_color(self):
        return self.__color

    def set_color(self, color):
        if color in self.COLOR_VARIANTS:
            self.__color = color
        else:
            print(f'Нельзя сменить цвет на {color}')

    def print_info(self):
        print(f'Модель: {self.__model}')
        print(f'Мощность двигателя: {self.__engine_power}')
        print(f'Цвет: {self.__color}')
        print(f'Владелец: {self.owner}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, engine_power, color):
        super().__init__(owner, model, engine_power, color)


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
# Изначальные свойства
vehicle1.print_info()
# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
# Проверяем что поменялось
vehicle1.print_info()
