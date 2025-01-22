# Старий інтерфейс, який можна адаптувати
class OldPrinter:
    def old_print(self, text):
        print(f"Old Printer: {text}")

# Новий інтерфейс, який очікує клієнтський код
class NewPrinter:
    def print_text(self, text):
        pass

# Адаптер, що дозволяє використовувати старий інтерфейс як новий
class PrinterAdapter(NewPrinter):
    def __init__(self, old_printer: OldPrinter):
        self.old_printer = old_printer

    def print_text(self, text):
        self.old_printer.old_print(text)

# Клієнтський код
def client_code(printer: NewPrinter):
    printer.print_text("Hello, world!")

# Використання
old_printer = OldPrinter()
adapter = PrinterAdapter(old_printer)

client_code(adapter)  # Виведе: Old Printer: Hello, world!
