import unittest
from datetime import datetime
from model.battery.nubbin_battery import NubbinBattery
from model.battery.spindler_battery import SpindlerBattery


class TestNubbing(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        battery = NubbinBattery(today,last_service_date)
        self.assertTrue(battery)

class TestNubbing(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        battery = SpindlerBattery(today, last_service_date)
        self.assertTrue(battery)


if __name__ == '__main__':
    unittest.main()