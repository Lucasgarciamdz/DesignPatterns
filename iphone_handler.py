from abstract_handler import AbstractHandler


class IPhoneHandler(AbstractHandler):
    def handle(self, request):
        if request == "iPhone":
            return "IPhoneHandler: Handling the request."
        else:
            return super().handle(request)


class IMacHandler(AbstractHandler):
    def handle(self, request):
        if request == "iMac":
            return "IMacHandler: Handling the request."
        else:
            return super().handle(request)


class DefaultHandler(AbstractHandler):
    def handle(self, request):
        return "DefaultHandler: No handler could process the request."
