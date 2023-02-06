class Warrior:
    def __init__(self):
        self.health = 100
        self.stamina = 100


class Mage:
    def __init__(self):
        self.health = 60
        self.mana = 100

unit1 = Warrior()
unit2 = Warrior()
unit3 = Mage()


unit2.healt = 100
unit2.stamina = 100

print(unit3.__dict__)
print(unit3.__dict__)

print(unit1.__dict__)
print(unit2.__dict__)

