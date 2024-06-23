class House:
    def __init__(self, name, num_of_floors):
        self.name = name
        self.num_of_floors = num_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.num_of_floors:
            print('Такого этажа не существует')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)


h1 = House('ЖК КРИСТАЛЛ', 3)
h1.go_to(2)
