class Observer:
    def update(self, message):
        raise NotImplementedError("Цей метод слід перевизначити.")

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class ConcreteObserverA(Observer):
    def update(self, message):
        print(f"ConcreteObserverA отримав: {message}")

class ConcreteObserverB(Observer):
    def update(self, message):
        print(f"ConcreteObserverB отримав: {message}")

# Використання
subject = Subject()

observer_a = ConcreteObserverA()
observer_b = ConcreteObserverB()

subject.attach(observer_a)
subject.attach(observer_b)

# Зміна стану суб'єкта і сповіщення спостерігачів
subject.notify("Стан змінився!")

# Відключення одного зі спостерігачів
subject.detach(observer_a)
subject.notify("Чергова зміна стану!")
