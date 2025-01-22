from abc import ABC, abstractmethod

# Реалізація інтерфейсу
class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class TV(Device):
    def turn_on(self):
        print("Телевізор увімкнуто")

    def turn_off(self):
        print("Телевізор вимкнено")

class Radio(Device):
    def turn_on(self):
        print("Радіо включено")

    def turn_off(self):
        print("Радіо вимкнено")

# Абстракція
class RemoteControl:
    def __init__(self, device: Device):
        self.device = device

    def toggle_power(self):
        self.device.turn_on()

# Розширена абстракція
class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        print("Пристрій вимкнено")

# Використання
tv = TV()
radio = Radio()

tv_remote = RemoteControl(tv)
tv_remote.toggle_power()  # Виведе: Телевізор увімкнуто

radio_remote = AdvancedRemoteControl(radio)
radio_remote.toggle_power()  # Виведе: Радіо включено
radio_remote.mute()          # Виведе: Пристрій вимкнено
