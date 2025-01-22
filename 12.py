from abc import ABC, abstractmethod
import time

# Інтерфейс предмета
class Image(ABC):
    @abstractmethod
    def display(self):
        pass

# Реальний предмет
class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_image_from_disk()

    def load_image_from_disk(self):
        print(f"Завантаження {self.filename} з диска...")
        time.sleep(2)  # Імітація тривалого завантаження

    def display(self):
        print(f"Відображення {self.filename}")

# Замісник
class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self._real_image = None

    def display(self):
        if self._real_image is None:
            self._real_image = RealImage(self.filename)  # Ліниве завантаження
        self._real_image.display()

# Використання
print("Створення об’єкта зображення проксі...")
image = ProxyImage("photo.jpg")

print("\nПерший виклик для відображення():")
image.display()  # Завантажить і відобразить зображення

print("\nДругий виклик для відображення():")
image.display()  # Використовує вже завантажене зображення без повторного завантаження
