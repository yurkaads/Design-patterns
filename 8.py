from abc import ABC, abstractmethod

# Абстрактний компонент
class Graphic(ABC):
    @abstractmethod
    def draw(self):
        pass

# Примітивний елемент
class Circle(Graphic):
    def draw(self):
        print("Малювання кола")

class Square(Graphic):
    def draw(self):
        print("Малювання квадрата")

# Складений елемент
class CompositeGraphic(Graphic):
    def __init__(self):
        self._children = []

    def add(self, graphic: Graphic):
        self._children.append(graphic)

    def remove(self, graphic: Graphic):
        self._children.remove(graphic)

    def draw(self):
        for child in self._children:
            child.draw()

# Використання
circle1 = Circle()
circle2 = Circle()
square = Square()

composite = CompositeGraphic()
composite.add(circle1)
composite.add(circle2)
composite.add(square)

# Викликає метод draw() для всіх компонентів у складі composite
composite.draw()
# Виведе:
# Малювання кола
# Малювання кола
# Малювання квадрата
