```markdown
# Mastering Python Warp Drive

This project is a simulation of a spaceship with a warp drive. The spaceship can engage its warp drive if it is functional, and repair it if it is not. The warp drive status can be checked at any time.

## Files

- `main.py`: The main entry point of the application.
- `warp_drive.py`: Contains the WarpDrive class, which represents the spaceship's warp drive.
- `ship.py`: Contains the Ship class, which represents the spaceship. A ship has a name and a warp drive.
- `utils.py`: Contains utility functions for generating a random ship name, checking the warp drive status, and repairing the warp drive.
- `tests.py`: Contains unit tests for the Ship and utility methods.
- `README.md`: This file, which provides an overview of the project.

## Usage

To run the application, execute the `main.py` file.

```bash
python main.py
```

To run the tests, execute the `tests.py` file.

```bash
python tests.py
```

## Code Snippets

Here are some code snippets from the project.

### ship.py

```python
class Ship:
    def __init__(self, name, warp_drive):
        self.name = name
        self.warp_drive = warp_drive

    def engage_warp(self):
        if self.warp_drive.is_functional():
            print(f"{self.name} is engaging warp drive!")
            self.warp_drive.activate()
        else:
            print(f"{self.name}'s warp drive is not functional.")

    def repair_warp_drive(self):
        print(f"Repairing {self.name}'s warp drive...")
        self.warp_drive.repair()
```

### utils.py

```python
import random

def generate_ship_name():
    """
    Generate a random ship name.
    """
    prefixes = ['USS', 'SS', 'HMS', 'RMS']
    names = ['Enterprise', 'Voyager', 'Discovery', 'Endeavour', 'Challenger', 'Atlantis', 'Columbia']
    return f"{random.choice(prefixes)} {random.choice(names)}"

def check_warp_drive_status(warp_drive):
    """
    Check the status of the warp drive.
    """
    if warp_drive.is_functional():
        return "Warp drive is functional."
    else:
        return "Warp drive is not functional."

def repair_warp_drive(warp_drive):
    """
    Repair the warp drive.
    """
    if not warp_drive.is_functional():
        print("Warp drive is not functional. Repairing...")
        warp_drive.repair()
        if warp_drive.is_functional():
            print("Warp drive is now functional.")
        else:
            print("Failed to repair warp drive.")
    else:
        print("Warp drive is functional. No need for repair.")
```

### tests.py

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
```
