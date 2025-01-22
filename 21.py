from abc import ABC, abstractmethod

# Базовий клас
class AbstractClass(ABC):
    def template_method(self):
        self.step1()
        self.step2()
        self.step3()

    @abstractmethod
    def step1(self):
        pass

    @abstractmethod
    def step2(self):
        pass

    def step3(self):
        print("Крок 3: загальний крок виконано.")

# Конкретний підклас A
class ConcreteClassA(AbstractClass):
    def step1(self):
        print("ConcreteClassA: Крок 1 виконано.")

    def step2(self):
        print("ConcreteClassA: Крок 2 виконано.")

# Конкретний підклас B
class ConcreteClassB(AbstractClass):
    def step1(self):
        print("ConcreteClassB: Крок 1 виконано.")

    def step2(self):
        print("ConcreteClassB: Крок 2 виконано.")

# Використання
print("Виконується ConcreteClassA:")
class_a = ConcreteClassA()
class_a.template_method()

print("\Виконується ConcreteClassB:")
class_b = ConcreteClassB()
class_b.template_method()
