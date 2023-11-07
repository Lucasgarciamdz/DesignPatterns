
def client_code(handler):
    for product in ["iPhone", "iMac", "iPad"]:
        print(f"\nClient: Who wants to handle {product}?")
        result = handler.handle(product)
        if result:
            print(f"  {result}")
        else:
            print("  No handler could process the request.")
