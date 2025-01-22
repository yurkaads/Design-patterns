class Mediator:
    def send(self, message, colleague):
        raise NotImplementedError("Цей метод слід перевизначити.")

class Colleague:
    def __init__(self, mediator):
        self.mediator = mediator

class ConcreteColleagueA(Colleague):
    def send_message(self, message):
        print(f"Колега А надсилає: {message}")
        self.mediator.send(message, self)

class ConcreteColleagueB(Colleague):
    def send_message(self, message):
        print(f"Колега Б надсилає: {message}")
        self.mediator.send(message, self)

class ConcreteMediator(Mediator):
    def __init__(self, colleague_a: ConcreteColleagueA, colleague_b: ConcreteColleagueB):
        self.colleague_a = colleague_a
        self.colleague_b = colleague_b

    def send(self, message, colleague):
        if colleague == self.colleague_a:
            self.colleague_b.receive_message(message)
        else:
            self.colleague_a.receive_message(message)

class ConcreteColleagueA(Colleague):
    def send_message(self, message):
        print(f"Колега А надсилає: {message}")
        self.mediator.send(message, self)

    def receive_message(self, message):
        print(f"Колега А отримав: {message}")

class ConcreteColleagueB(Colleague):
    def send_message(self, message):
        print(f"Колега Б надсилає: {message}")
        self.mediator.send(message, self)

    def receive_message(self, message):
        print(f"Колега Б отримав: {message}")

# Використання
mediator = ConcreteMediator(ConcreteColleagueA(Mediator), ConcreteColleagueB(Mediator))

# Взаємодія між учасниками через посередника
mediator.colleague_a.send_message("Привіт, колего Б!")
mediator.colleague_b.send_message("Привіт, колего A!")
