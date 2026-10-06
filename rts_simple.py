

class Knight(object):
    def __init__(self, level):
        self.unit_type = "Knight"
        if level == 1:
            self.life = 400
            self.speed = 5
            self.attack_power = 3
            self.attack_range = 2
            self.weapon = "Short Sword"

        elif level == 2:
            self.life = 400
            self.speed = 5
            self.attack_power = 4
            self.attack_range = 3
            self.weapon = "Medium Sword"

    def __str__(self):
        return "Unit Type: {0}" \
               "Life: {1}\n" \
               "Speed: {2}\n" \
               "Attack Power {3}\n" \
               "Attack Range {4}\n" \
               "Weapon: {5}".format(
                   self.unit_type,
                   self.life,
                   self.speed,
                   self.attack_power,
                   self.attack_range,
                   self.weapon
               )

class Archer(object):
    def __init__(self, level):
        self.unit_type = "Archer"
        if level == 1:
            self.life = 200
            self.speed = 7
            self.attack_power = 1
            self.attack_range = 3
            self.weapon = "Short Bowl"

        elif level == 2:
            self.life = 200
            self.speed = 7
            self.attack_power = 2
            self.attack_range = 4
            self.weapon = "Medium Bowl"

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

class Calvary(object):
    def __init__(self, level):
        self.unit_type = "Calvary"
        if level == 1:
            self.life = 700
            self.speed = 4
            self.attack_power = 5
            self.attack_range = 2
            self.weapon = "Small Shield"

        if level == 2:
            self.life = 700
            self.speed = 4
            self.attack_power = 6
            self.attack_range = 3
            self.weapon = "Small Shield"

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
        elif unit_type.lower() == "calvary":
            return Calvary(level)



if __name__ == "__main__":
    barrack = Barrack()
    knight1 = barrack.build_units("Knight", 1)
    archer1 = barrack.build_units("Archer", 2)
    calvary1 = barrack.build_units("Calvary", 2)
    print("[Knight1] {}".format(knight1))
    print("[Archer1] {}".format(archer1))
    print("[Calvary1] {}".format(calvary1))
        
    
        