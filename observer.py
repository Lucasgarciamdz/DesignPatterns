from __future__ import annotations
from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, observable: Observable, *args):
        pass


class Observable(ABC):
    def __init__(self):
        self.observers = []

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def delete_observer(self, observer: Observer):
        self.observers.remove(observer)

    def notify_observers(self, *args):
        for observer in self.observers:
            observer.update(self, *args)
