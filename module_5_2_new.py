class House:
    def __init__(self, name, num_of_floors):
        self.name = name
        self.num_of_floors = num_of_floors

    def __len__(self):
        return self.num_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей:{self.num_of_floors}"

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.num_of_floors:
            print('Такого этажа не существует')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)


h1 = House('ЖК КРИСТАЛЛ', 4)
h2 = House('ЖК УСТАЛ', 10)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
