class Memento:
    def __init__(self, state):
        self.state = state

class Originator:
    def __init__(self):
        self.state = None

    def set_state(self, state):
        print(f"Оригінатор: встановлення стану на {state}")
        self.state = state

    def create_memento(self):
        return Memento(self.state)

    def restore_memento(self, memento):
        self.state = memento.state
        print(f"Оригінатор: відновлено стан до {self.state}")

class Caretaker:
    def __init__(self):
        self.mementos = []

    def save(self, originator):
        self.mementos.append(originator.create_memento())

    def restore(self, originator, index):
        if 0 <= index < len(self.mementos):
            originator.restore_memento(self.mementos[index])
        else:
            print("Доглядач: Недійсний індекс сувеніру.")

# Використання
caretaker = Caretaker()
originator = Originator()

originator.set_state("Стан 1")
caretaker.save(originator)

originator.set_state("Стан 2")
caretaker.save(originator)

originator.set_state("Стан 3")

print("\nПовернення до попереднього стану:")
caretaker.restore(originator, 1)  # Відновлення до "Стан 2"
caretaker.restore(originator, 0)  # Відновлення до "Стан 1"
