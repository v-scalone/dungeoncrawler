from termcolor import cprint
from visual import tprint

class Player:
    def __init__(self, name, type="Human"):
        self.name = name
        self.type = type
        self.level = 1
        self._xp = 0
        self.hp = 50
        self.armor = 0

    def lvl_up(self, xp_amt):
        self.xp += xp_amt
        while self._xp >= 100:
            self._xp -= 100
            self.level += 1
            tprint(f"Congrats, you are now level {self.level}!", "green")
        tprint(f"Current XP: {self.xp}")
