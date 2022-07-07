from types import NoneType
from termcolor import cprint
from weapons import Weapon
from visual import tprint
from monster import Monster
from sys import exit

class Player:
    def __init__(self, name, type="Human"):
        self.name = name
        self.type = type
        self.level = 1
        self._xp = 0
        self.hp = 50
        self.armor = None
        self.weapon = None
        self.strength = 2
    
    def equip_weapon(self, new_weapon):
        self.weapon = new_weapon
        tprint(f"You have equipped {self.weapon.type}!\nYour damage is now {self.strength + self.weapon.damage}!", color="green")
    
    def equip_armor(self, new_armor):
        self.armor = new_armor
        tprint(f"You have equipped {self.armor.type} armor!\nYour armor level is now {self.armor.hits}!", color="green")


    def lvl_up(self, xp_amt):
        self.xp += xp_amt
        while self._xp >= 100:
            self._xp -= 100
            self.level += 1
            tprint(f"Congrats, you are now level {self.level}!", "green")
        tprint(f"Current XP: {self.xp}")

    def fight(self, monster):
        tprint("You chose to fight!", color="magenta")
        monster.hit(self, self.strength + self.weapon.damage)

    def _take_damage(self, amount):
        if self.armor:  #checks if player has armor
            if self.armor.hits >= amount: #if player has enough armor to take all the hits, armor gets damaged
                for i in range(amount):
                    self.armor.hits -= 1
                    amount -= 1
                if self.armor.hits == 0: #checks if armor is broken after fight
                    self.armor = None 
                    tprint(f"Oh no!\nYour armor broke in fight :(", color="red")
            if self.armor.hits < amount:    #if player doesn't have enough armor to take all hits, armor gets used up
                for i in range(self.armor.hits):
                    self.armor.hits -= 1
                    amount -= 1 
                self.armor = None 
                tprint(f"Oh no!\nYour armor broke in fight :(", color="red")
        if amount:  #this happens when armor got used up or if there was no armor, as amount will be 0 if armor took all the hits!
            if self.hp > amount:
                self.hp -= amount
                tprint(f"You took a hit!\nYour remaining HP is: {self.hp}",color="red")
            else:
                tprint("You DIED!\nGAME OVER", color="red")
                exit()



sword = Weapon("sword", 3)
p = Player("vic")
p.equip_weapon(sword)
m = Monster("Slime", 6, 10)
p.fight(m)