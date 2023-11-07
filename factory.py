from abstract_factory import AbstractFactory
from products import IPhone, IMac


class AppleFactory(AbstractFactory):
    def create_product(self, product_type=None, color=None, processor=None):
        if product_type == 'iPhone':
            return IPhone(color, processor)
        elif product_type == 'iMac':
            return IMac(color, processor)
        else:
            raise ValueError("Invalid product type.")
