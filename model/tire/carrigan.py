from .tire import Tire


class CarriganTire(Tire):
    def __init__(self, wear):
        self.wear = wear

    def needs_service(self):
        for i in range(len(self.wear)):
            if self.wear[i] >= 0.9:
                return True
            else:
                return False
