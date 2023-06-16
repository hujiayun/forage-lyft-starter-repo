from model.car.car import Car
from model.engine.capulet_engine import CapuletEngine
from model.engine.sternman_engine import SternmanEngine
from model.engine.willoughby_engine import WilloughbyEngine
import unittest
from datetime import datetime


class TestCalliope_Engine(unittest.TestCase):
    def test_engine_serviced(self):
        current_mileage = 0
        last_service_mileage = 100
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.engine_should_be_serviced())


class TestSternman_Engine(unittest.TestCase):
    def test_engine_serviced(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.engine_should_be_serviced())


class TestWilloughby_Engine(unittest.TestCase):
    def test_engine_serviced(self):
        current_mileage = 60800
        last_service_mileage = 100
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.engine_should_be_serviced())


if __name__ == '__main__':
    unittest.main()
