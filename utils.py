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
