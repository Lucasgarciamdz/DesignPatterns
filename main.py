from apple_store import AppleStore
from client import Client


def main():
    store = AppleStore()
    client1 = Client('Client 1')
    client2 = Client('Client 2')

    store.add_observer(client1)
    store.add_observer(client2)

    store.product = 'iPhone 15'


if __name__ == '__main__':
    main()
