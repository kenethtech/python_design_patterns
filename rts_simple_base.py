
class Knight(object):
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
               "Attack Range {4}\n" \
               "Weapon: {5}".format(
                   self.unit_type,
                   self.life,
                   self.speed,
                   self.attack_power,
                   self.attack_range,
                   self.weapon
               )

class Archer(object): #Creating the archer class with archer attributes
    def __init__(self, level):
        self.unit_type = "archer"
        filename = "{}_{}.dat".format(self.unit_type, level)
        with open(filename, "r") as f:  #Read the file line by line
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

class Barrack(object):
    def build_units(self, unit_type, level):
        if unit_type.lower() == "knight":
            return Knight(level)

        elif unit_type.lower() == "archer":
            return Archer(level)


if __name__ == "__main__":
    barrack = Barrack()
    knight1 = barrack.build_units("knight", 1)
    archer1 = barrack.build_units("archer", 1)

    print("[Knight1] {}".format(knight1))
    print("[Archer1] {}".format(archer1))