from transportes import Truck, Ship


class TransportFactory:
    def create_transport(self, transport_type):
        if transport_type == 'Truck':
            return Truck()
        elif transport_type == 'Ship':
            return Ship()
        else:
            raise ValueError("Tipo de transporte inválido.")
