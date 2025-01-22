from abc import ABC, abstractmethod

# Інтерфейс елемента
class Element(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# Конкретний елемент A
class ConcreteElementA(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_a(self)

    def operation_a(self):
        return "ConcreteElementA: Операція А."

# Конкретний елемент B
class ConcreteElementB(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_b(self)

    def operation_b(self):
        return "ConcreteElementB: Операція B."

# Інтерфейс відвідувача
class Visitor(ABC):
    @abstractmethod
    def visit_concrete_element_a(self, element):
        pass

    @abstractmethod
    def visit_concrete_element_b(self, element):
        pass

# Конкретний відвідувач
class ConcreteVisitor(Visitor):
    def visit_concrete_element_a(self, element):
        print(f"Відвідувач: {element.operation_a()}")

    def visit_concrete_element_b(self, element):
        print(f"Відвідувач: {element.operation_b()}")

# Використання
elements = [ConcreteElementA(), ConcreteElementB()]
visitor = ConcreteVisitor()

for element in elements:
    element.accept(visitor)
