from .tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, wear):
        self.wear = wear

    def needs_service(self):
        w_sum = 0
        for i in range(len(self.wear)):
            w_sum += self.wear[i]
        if w_sum >= 3:
            return True
        else:
            return False
