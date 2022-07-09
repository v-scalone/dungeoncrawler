from termcolor import cprint
from visual import tprint

class Weapon:

    

    def __init__(self, type, damage, condition=3):
        self.type = type
        self.damage = damage
        self.condition = condition
        self.uses = 0
        self._condition_lookup = {0: "broken", 1: "damaged", 2: "used", 3: "flawless"}

    def use(self):
        self.uses += 1
        if self.uses == 10:
            self.uses = 0
            self.condition -= 1

    def repair(self, amount=1):
        for i in range(amount):
            if self.condition == 3:
                tprint(
                    "This weapon cannot be repaired, it is already in flawless condition!",
                    color="green")
                return amount
            else:
                self.condition += 1
                amount -= 1
                tprint(
                    f"Success! Your {self.type.capitalize()} is now in {self._condition_lookup[self.condition]} condition!",
                    color="green",)


class Sword(Weapon):
    def __init__(self, damage, condition=3):
        super().__init__("melee", damage, condition)
    pass

if __name__ == "__main__":
    weap = Weapon("melee", 5, 2)
    weap.repair(1)