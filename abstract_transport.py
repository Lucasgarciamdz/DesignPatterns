from abc import ABC, abstractmethod


class AbstractTransport(ABC):
    @abstractmethod
    def deliver(self):
        pass
