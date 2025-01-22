class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Ініціалізація відбувається лише під час першого створення екземпляра
            cls._instance.data = []
        return cls._instance

    def add_data(self, value):
        self.data.append(value)

    def get_data(self):
        return self.data


# Використання
singleton1 = Singleton()
singleton2 = Singleton()

singleton1.add_data("Перший запис")
singleton2.add_data("Другий запис")

print(singleton1.get_data())  # ['Перший запис', 'Другий запис']
print(singleton2.get_data())  # ['Перший запис', 'Другий запис']
print(singleton1 is singleton2)  # True, обидва посилаються на один екземпляр
