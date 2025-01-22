from abc import ABC, abstractmethod

# Абстрактний продукт
class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass

# Конкретні продукти
class Truck(Transport):
    def deliver(self):
        print("Доставка наземним транспортом в ящику.")

class Ship(Transport):
    def deliver(self):
        print("Доставка морем в контейнері.")

# Абстрактна фабрика
class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        pass

# Конкретні фабрики
class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()

class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()

# Використання
def plan_delivery(logistics: Logistics):
    transport = logistics.create_transport()
    transport.deliver()

# Приклад використання
road_logistics = RoadLogistics()
sea_logistics = SeaLogistics()

plan_delivery(road_logistics)  # Виведе: "Доставка наземним транспортом в ящику."
plan_delivery(sea_logistics)    # Виведе: "Доставка морем в контейнері."
