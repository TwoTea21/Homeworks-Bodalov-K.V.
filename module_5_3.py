class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        instance = super(House, cls).__new__(cls)
        if len(args) > 0:
            cls.houses_history.append(args[0])
            return instance

    def __del__(self):
        print(f"{self.name} снесён, какая грусть...(")

    def __init__(self, name, num_of_floors, *args, ):
        self.name = name
        self.num_of_floors = num_of_floors

    def __eq__(self, other):
        self.other = other
        if self.num_of_floors == self.other:
            return True
        else:
            return False

    def __add__(self, value):
        if isinstance(value, House):
            return House(f"{self.name} + {value.name}", self.num_of_floors + value.num_of_floors)
        elif isinstance(value, int):
            return House(self.name, self.num_of_floors + value)
        return NotImplemented

    def __iadd__(self, value):
        if isinstance(value, House):
            return House(f"{self.name} + {value.name}", self.num_of_floors + value.num_of_floors)
        elif isinstance(value, int):
            return House(self.name, self.num_of_floors + value)
        return NotImplemented

    def __radd__(self, value):
        if isinstance(value, House):
            return House(f"{self.name} + {value.name}", self.num_of_floors + value.num_of_floors)
        elif isinstance(value, int):
            return House(self.name, self.num_of_floors + value)
        return NotImplemented

    def __len__(self):
        return self.num_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей:{self.num_of_floors}"

    def __lt__(self, other):
        return self.num_of_floors > other.num_of_floors

    def __le__(self, other):
        return self.num_of_floors <= other.num_of_floors

    def __gt__(self, other):
        return self.num_of_floors > other.num_of_floors

    def __ge__(self, other):
        return self.num_of_floors >= other.num_of_floors

    def __ne__(self, other):
        return self.num_of_floors != other.num_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.num_of_floors:
            print('Такого этажа не существует')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)


h1 = House('ЖК КРИСТАЛЛ', 10)
print(House.houses_history)
h2 = House('ЖК УСТАЛ', 20)
print(House.houses_history)
h3 = House('ЖК ЗВЕЗДА', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
