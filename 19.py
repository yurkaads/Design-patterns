class State:
    def handle(self):
        raise NotImplementedError("Цей метод слід перевизначити.")

class ConcreteStateA(State):
    def handle(self):
        print("Стан A: обробка запиту та перехід до стану B.")
        return ConcreteStateB()

class ConcreteStateB(State):
    def handle(self):
        print("Стан B: обробка запиту та перехід до стану A.")
        return ConcreteStateA()

class Context:
    def __init__(self):
        self.state = ConcreteStateA()  # Початковий стан

    def request(self):
        self.state = self.state.handle()  # Виклик методу стану

# Використання
context = Context()

for _ in range(4):  # Виконуємо декілька запитів
    context.request()
