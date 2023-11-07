from iphone_builder import IPhoneBuilder, Director


def main():
    director = Director()
    builder = IPhoneBuilder()
    director.builder = builder

    director.build_minimal_product()
    iphone = builder.get_result()
    print(iphone)


if __name__ == "__main__":
    main()
