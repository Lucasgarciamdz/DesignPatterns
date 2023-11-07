from abc import ABC, abstractmethod


class IPhone:
    def __init__(self):
        self.color = None
        self.processor = None

    def __str__(self):
        return f"iPhone color: {self.color}, processor: {self.processor}"


class AbstractBuilder(ABC):
    @abstractmethod
    def set_color(self, color):
        pass

    @abstractmethod
    def set_processor(self, processor):
        pass

    @abstractmethod
    def get_result(self):
        pass
