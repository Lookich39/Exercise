class Tomato():
    states = {0: 'пусто', 1: 'цветок', 2: 'зеленый помидор', 3: 'красный помидор'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        self._state += 1

    def is_ripe(self):
        if self._state == 3:
            return True
        else:
            return False


class TomatoBush():
    def __init__(self, amount):
        self.amount = amount
        self.tomatoes = [Tomato(index) for index in range(0, amount - 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []


class Gardener():

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()
        print("Обработал растение")