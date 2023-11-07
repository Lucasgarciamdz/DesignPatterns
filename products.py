from abstract_factory import AbstractProduct


class IPhone(AbstractProduct):
    def interact(self):
        return f"You've created an iPhone with color {self.color} and processor {self.processor}."


class IMac(AbstractProduct):
    def interact(self):
        return f"You've created an iMac with color {self.color} and processor {self.processor}."
