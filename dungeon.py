from random import randrange, choice
from visual import tprint
from monster import Monster

class Room:
    def __init__(self, monster_prob=3, chest_prob=5):
        self.monster_prob = monster_prob
        self.chest_prob = chest_prob

    def enter(self):
        if randrange(self.monster_prob) == 0:
            type = choice(("slime", "skeleton", "ghost", ))
            monster = Monster(type, randrange(1,5))
            tprint(f"OH NO!\nA {type} guards this room! What do you want to do?")
            
            pass