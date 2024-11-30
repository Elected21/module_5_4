class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        instance = object.__new__(cls)
        cls.houses_history.append(args[0])
        return instance

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            return f'Нельзя сравнивать объекты разных классов/типов'

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            return f'Нельзя сравнивать объекты разных классов/типов'

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            return f'Нельзя сравнивать объекты разных классов/типов'

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            return f'Нельзя сравнивать объекты разных классов/типов'

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            return f'Нельзя сравнивать объекты разных классов/типов'

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            return f'Нельзя сравнивать объекты разных классов/типов'

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        else:
            print('Значение слагаемого должно быть целочисленным типом')
        return self

    def __iadd__(self, value):
        self.__add__(value)
        return self

    def __radd__(self, value):
        self.__add__(value)
        return self

    def __del__(self):
        return print(f'{self.name} снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

h2 = House('ЖК Акация', 20)
print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)


# Удаление объектов
del h2
del h3

print(House.houses_history)