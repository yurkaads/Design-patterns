from abc import ABC, abstractmethod

# Базовий інтерфейс
class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass

# Конкретний клас
class SimpleCoffee(Coffee):
    def cost(self):
        return 5

    def description(self):
        return "Проста кава"

# Базовий декоратор
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

    def description(self):
        return self._coffee.description()

# Конкретні декоратори
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2

    def description(self):
        return f"{self._coffee.description()} + молоко"

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1

    def description(self):
        return f"{self._coffee.description()} + цукор"

# Використання
coffee = SimpleCoffee()
print(coffee.description(), "-", coffee.cost())  # Проста кава - 5

# Додаємо молоко
coffee_with_milk = MilkDecorator(coffee)
print(coffee_with_milk.description(), "-", coffee_with_milk.cost())  # Проста кава + молоко - 7

# Додаємо цукор
coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)
print(coffee_with_milk_and_sugar.description(), "-", coffee_with_milk_and_sugar.cost())  # Проста кава + молоко + цукор - 8
