from abc import ABC, abstractmethod

# Інтерфейс для команд
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Виконавець, що виконує конкретні дії
class Light:
    def turn_on(self):
        print("Світло горить")

    def turn_off(self):
        print("Світло ВИМКНЕНО")

# Конкретні команди
class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_on()

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_off()

# Відправник, що запускає команди
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command: Command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()

# Використання
light = Light()
light_on = LightOnCommand(light)
light_off = LightOffCommand(light)

remote = RemoteControl()
remote.set_command(light_on)
remote.press_button()  # Вмикає світло

remote.set_command(light_off)
remote.press_button()  # Вимикає світло
