from abc import ABC, abstractmethod

# Абстрактні продукти
class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        pass

class Sofa(ABC):
    @abstractmethod
    def lie_on(self):
        pass

# Конкретні продукти для сімейства "Вікторіанський стиль"
class VictorianChair(Chair):
    def sit_on(self):
        print("Сидячи на Вікторіанському стільці.")

class VictorianSofa(Sofa):
    def lie_on(self):
        print("Лежачи на Вікторіанському дивані.")

# Конкретні продукти для сімейства "Модерн стиль"
class ModernChair(Chair):
    def sit_on(self):
        print("Сидячи на сучасному стільці.")

class ModernSofa(Sofa):
    def lie_on(self):
        print("Лежачи на сучасному дивані.")

# Абстрактна фабрика
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass

# Конкретні фабрики для створення меблів у різних стилях
class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_sofa(self) -> Sofa:
        return VictorianSofa()

class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_sofa(self) -> Sofa:
        return ModernSofa()

# Використання
def furnish_room(factory: FurnitureFactory):
    chair = factory.create_chair()
    sofa = factory.create_sofa()
    chair.sit_on()
    sofa.lie_on()

# Приклад використання
victorian_factory = VictorianFurnitureFactory()
modern_factory = ModernFurnitureFactory()

furnish_room(victorian_factory)  # Використовує вікторіанський стиль меблів
furnish_room(modern_factory)     # Використовує сучасний стиль меблів
