from random import randrange
from visual import tprint
from monster import monster

class Room:
    def __init__(self, monster_prob=3, chest_prob=5):
        self.monster_prob = monster_prob
        self.chest_prob = chest_prob

    def enter(self):
        if randrange(self.monster_prob) == 0:
            #monster will spawn
            pass
        
