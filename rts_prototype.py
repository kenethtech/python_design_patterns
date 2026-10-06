from prototype_1 import Prototype
from copy import deepcopy

class Knight(Prototype):
    def __init__(self, level):
        self.unit_type = "knight"
        filename = "{}_{}.dat".format(self.unit_type, level)
        with open(filename, "r") as f:
            lines = f.read().split("\n")
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[4]

    def __str__(self):
        return "Unit Type: {0}\n" \
               "Life: {1}\n" \
               "Speed: {2}\n" \
               "Attack Power: {3}\n" \
               "Attack Range: {4}\n" \
               "Weapon: {5}\n".format(
                   self.unit_type,
                   self.life,
                   self.speed,
                   self.attack_power,
                   self.attack_range,
                   self.weapon
               )

    def clone(self):
        return deepcopy(self)

class Archer(Prototype):
    def __init__(self,level):
        self.unit_type = "Archer"
        filename = "{}_{}.dat".format(self.unit_type, level)
        with open(filename, "r") as f:
            lines = f.read().split("\n")
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[4]

    def __str__(self):
        return "Unit Type: {0}\n" \
               "Life: {1}\n" \
               "Speed: {2}\n" \
               "Attack Power: {3}\n" \
               "Attack Range: {4}\n" \
               "Weapon: {5}".format(
                   self.unit_type,
                   self.life,
                   self.speed,
                   self.attack_power,
                   self.attack_range,
                   self.weapon
               )

    def clone(self):
        return deepcopy(self)

class Barrack(object):
    def __init__(self):
        self.unit_type = {
            "knight": {
                1: Knight(1),
                
            },
            "archer": {
                1: Archer(1),
                
            }
        }

    def build_units(self, unit_type, level):
        return self.unit_type[unit_type.lower()][level].clone()


if __name__ == "__main__":
    barrack = Barrack()
    knight1 = barrack.build_units("knight", 1)
    archer1 = barrack.build_units("Archer", 1)

    print("[Knight1] {}".format(knight1))
    print("[Archer2] {}".format(archer1) )
