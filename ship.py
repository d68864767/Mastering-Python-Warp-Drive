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
