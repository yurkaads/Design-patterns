class House:
    def __init__(self):
        self.has_walls = False
        self.has_roof = False
        self.has_garden = False

    def __str__(self):
        parts = [
            "стіни" if self.has_walls else "немає стін",
            "дах" if self.has_roof else "немає даху",
            "сад" if self.has_garden else "немає саду"
        ]
        return f"Будинок з {', '.join(parts)}."


# Будівельник, що визначає етапи побудови
class HouseBuilder:
    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.has_walls = True
        return self

    def build_roof(self):
        self.house.has_roof = True
        return self

    def build_garden(self):
        self.house.has_garden = True
        return self

    def get_result(self):
        return self.house


# Директор, який контролює процес побудови
class Director:
    @staticmethod
    def construct_simple_house(builder: HouseBuilder):
        return builder.build_walls().build_roof().get_result()

    @staticmethod
    def construct_luxury_house(builder: HouseBuilder):
        return builder.build_walls().build_roof().build_garden().get_result()


# Використання
builder = HouseBuilder()
simple_house = Director.construct_simple_house(builder)
print(simple_house)  # Будинок зі стінами, дахом, без саду.

luxury_house = Director.construct_luxury_house(builder)
print(luxury_house)  # Будинок зі стінами, дахом, садом.
