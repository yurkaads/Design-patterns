import copy

# Клас-прототип
class Car:
    def __init__(self, model, color, features=None):
        self.model = model
        self.color = color
        self.features = features or []

    def add_feature(self, feature):
        self.features.append(feature)

    def clone(self):
        # Повертає поверхневу копію об'єкта
        return copy.copy(self)

    def __str__(self):
        return f"Car(model={self.model}, color={self.color}, features={self.features})"


# Використання
original_car = Car("Седан", "Червоний")
original_car.add_feature("Кондиціонер")
original_car.add_feature("Люк")

# Клонування об'єкта
cloned_car = original_car.clone()
cloned_car.color = "Синій"  # Змінюємо колір у клоні
cloned_car.add_feature("Шкіряні сидіння")

print("Оригінальний автомобіль:", original_car)  # Car(model=Седан, color=Червоний, features=['Кондиціонер', 'Люк'])
print("Клонований автомобіль:", cloned_car)      # Car(model=Седан, color=Синій, features=['Кондиціонер', 'Люк', 'Шкіряні сидіння'])
