from iphone_handler import IPhoneHandler, IMacHandler, DefaultHandler
from client_code import client_code


def main():
    iphone_handler = IPhoneHandler()
    imac_handler = IMacHandler()
    default_handler = DefaultHandler()

    iphone_handler.set_next(imac_handler).set_next(default_handler)

    client_code(iphone_handler)


if __name__ == "__main__":
    main()
