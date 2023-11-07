from observer import Observable


class AppleStore(Observable):
    def __init__(self):
        super().__init__()
        self._product = None

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        self._product = value
        self.notify_observers(value)
