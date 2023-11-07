from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_product(self):
        pass


class AbstractProduct(ABC):
    def __init__(self, color, processor):
        self.color = color
        self.processor = processor

    @abstractmethod
    def interact(self):
        pass
