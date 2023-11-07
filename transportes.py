from abstract_transport import AbstractTransport


class Truck(AbstractTransport):
    def deliver(self):
        return "Entrega realizada por camión."


class Ship(AbstractTransport):
    def deliver(self):
        return "Entrega realizada por barco."
