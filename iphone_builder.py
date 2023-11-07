from iphone import AbstractBuilder, IPhone


class IPhoneBuilder(AbstractBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = IPhone()

    def set_color(self, color):
        self._product.color = color
        return self

    def set_processor(self, processor):
        self._product.processor = processor
        return self

    def get_result(self):
        return self._product


class Director:
    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder):
        self._builder = builder

    def build_minimal_product(self):
        self.builder.set_color('Black').set_processor('A13')
