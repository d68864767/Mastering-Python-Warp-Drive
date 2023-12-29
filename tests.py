```python
import unittest
from ship import Ship
from warp_drive import WarpDrive
from utils import generate_ship_name, check_warp_drive_status, repair_warp_drive

class TestShipMethods(unittest.TestCase):

    def setUp(self):
        self.warp_drive = WarpDrive()
        self.ship = Ship(generate_ship_name(), self.warp_drive)

    def test_engage_warp(self):
        self.ship.engage_warp()
        self.assertEqual(self.ship.warp_drive.is_functional(), True)

    def test_repair_warp_drive(self):
        self.ship.repair_warp_drive()
        self.assertEqual(self.ship.warp_drive.is_functional(), True)

class TestUtilsMethods(unittest.TestCase):

    def setUp(self):
        self.warp_drive = WarpDrive()

    def test_check_warp_drive_status(self):
        status = check_warp_drive_status(self.warp_drive)
        self.assertIn(status, ["Warp drive is functional.", "Warp drive is not functional."])

    def test_repair_warp_drive(self):
        repair_warp_drive(self.warp_drive)
        self.assertEqual(self.warp_drive.is_functional(), True)

if __name__ == '__main__':
    unittest.main()
```
