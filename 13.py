from abc import ABC, abstractmethod

# Базовий клас для обробника
class Handler(ABC):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abstractmethod
    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)
        return None

# Конкретний обробник для позитивних чисел
class PositiveHandler(Handler):
    def handle(self, request):
        if request > 0:
            return f"PositiveHandler: Оброблено запит {request} (позитивне число)"
        else:
            return super().handle(request)

# Конкретний обробник для нуля
class ZeroHandler(Handler):
    def handle(self, request):
        if request == 0:
            return "ZeroHandler: Оброблено запит 0 (нуль)"
        else:
            return super().handle(request)

# Конкретний обробник для негативних чисел
class NegativeHandler(Handler):
    def handle(self, request):
        if request < 0:
            return f"NegativeHandler: Оброблено запит {request} (негативне число)"
        else:
            return super().handle(request)

# Створення ланцюжка обробників
negative_handler = NegativeHandler()
zero_handler = ZeroHandler(negative_handler)
positive_handler = PositiveHandler(zero_handler)

# Використання ланцюжка
requests = [10, -5, 0, 5]
for req in requests:
    result = positive_handler.handle(req)
    print(result)
