from observer import Observer
from observer import Observable


class Client(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, observable: Observable, *args):
        print(f'{self.name} received update from Apple Store: {args[0]} is now available')
