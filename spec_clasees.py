class House:
    def __init__(self):
        self.num_of_floors = 0

    def set_new_number_of_floors(self, floors):
        self.num_of_floors = floors
        print(self.num_of_floors)


h1 = House()
h1.set_new_number_of_floors(10)
