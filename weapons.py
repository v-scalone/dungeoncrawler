from termcolor import cprint

class Weapon:

    _condition_lookup = {0: "broken", 1: "damaged", 2: "used", 3: "flawless"}

    def __init__(self, type, damage, condition=3):
        self.type = type
        self.damage = damage
        self.condition = condition
        self.uses = 0

    def use(self):
        self.uses += 1
        if self.uses == 10:
            self.uses = 0
            self.condition -= 1

    def repair(self, amount=1):
        for i in range(amount):
            if self.conditon == 3:
                cprint("This weapon cannot be repaired, it is already in flawless condition!", "green")
                return amount
            else:
                self.condition += 1
                amount -= 1
                cprint(f"Success! Your {self.type.capitalize()} is now in {_condition_lookup[self.conditon]} condition!", "green", attrs=["blink"])


class Sword(Weapon):
    def __init__(self, damage, condition=3):
        super().__init__("melee", damage, condition)
    pass
