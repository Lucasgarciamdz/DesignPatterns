from command import Command


class Device:
    def turn_on(self):
        return "Device is turned on."

    def turn_off(self):
        return "Device is turned off."


class TurnOnCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        return self.device.turn_on()


class TurnOffCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        return self.device.turn_off()
