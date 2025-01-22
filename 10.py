# Підсистема 1
class CPU:
    def start(self):
        print("ЦП запускається")

    def execute(self):
        print("ЦП виконує команди")

# Підсистема 2
class Memory:
    def load(self):
        print("Пам'ять завантажує дані")

# Підсистема 3
class HardDrive:
    def read_data(self):
        print("Читання даних з жорсткого диска")

# Фасад
class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start_computer(self):
        print("Запуск комп'ютера...")
        self.cpu.start()
        self.memory.load()
        self.cpu.execute()
        self.hard_drive.read_data()
        print("Комп'ютер успішно запущено")

# Використання
computer = ComputerFacade()
computer.start_computer()
