from abstract_transport import TransportFactory


def main():
    factory = TransportFactory()
    transport = factory.create_transport('Truck')
    print(transport.deliver())


if __name__ == "__main__":
    main()
