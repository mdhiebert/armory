from enum import Enum
from os import name

class ItemStatus(Enum):
    MISSING = 0
    CHECKED_IN = 1
    CHECKED_OUT = 2
    UNKNOWN = 3

class Item:
    def __init__(self, item_id, item_name, serial_number):
        self.id = item_id
        self.name = item_name
        self.serial_number = serial_number

    def __eq__(self, other):
        return type(other) == type(self) and \
            self.id == other.id and \
            self.name == other.name and \
            self.serial_number == other.serial_number

    def __iter__(self):
        yield self.id
        yield self.name
        yield self.serial_number

class M4(Item):
    def __init__(self, item_id, serial_number):
        super().__init__(item_id, 'M4 Carbine', serial_number)

class M249(Item):
    def __init__(self, item_id, serial_number):
        super().__init__(item_id, 'M249 Squad Automatic Weapon', serial_number)

class M240(Item):
    def __init__(self, item_id, serial_number):
        super().__init__(item_id, 'M240', serial_number)

class M68CCO(Item):
    def __init__(self, item_id, serial_number):
        super().__init__(item_id, 'M68 Close Quarters Optic', serial_number)

class PEQ15(Item):
    def __init__(self, item_id, serial_number):
        super().__init__(item_id, 'EOTech ATPIAL AN/PEQ-15', serial_number)

class PVS14(Item):
    def __init__(self, item_id, serial_number):
        super().__init__(item_id, 'PVS-14 Night Vision Monocular', serial_number)

class M320(Item):
    def __init__(self, item_id, serial_number):
        super().__init__(item_id, 'M320 Grenade Launcher Module', serial_number)