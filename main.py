from factory import AppleFactory


def main():
    factory = AppleFactory()

    iphone = factory.create_product('iPhone', 'black', 'A13')
    print(iphone.interact())

    imac = factory.create_product('iMac', 'silver', 'M1')
    print(imac.interact())


if __name__ == "__main__":
    main()
