from abc import ABC, abstractmethod

# Інтерфейс стратегії
class Strategy(ABC):
    @abstractmethod
    def execute(self, data):
        pass

# Конкретна стратегія A
class ConcreteStrategyA(Strategy):
    def execute(self, data):
        print(f"ConcreteStrategyA: Обробка {data} зі стратегією А.")

# Конкретна стратегія B
class ConcreteStrategyB(Strategy):
    def execute(self, data):
        print(f"ConcreteStrategyB: Обробка {data} зі стратегією B.")

# Контекст
class Context:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy

    def execute_strategy(self, data):
        self.strategy.execute(data)

# Використання
context = Context(ConcreteStrategyA())
context.execute_strategy("Дані1")

context.set_strategy(ConcreteStrategyB())
context.execute_strategy("Дані2")
