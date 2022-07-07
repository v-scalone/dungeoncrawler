from visual import tprint

class Monster:
    def __init__(self, type, hp, strength):
        self.type = type
        self.hp = hp
        self.state = True
        self.strength = strength

    def hit(self, player,  amount):
        for i in range(amount):
            if self.hp > amount:
                self.hp -= 1
            else:
                tprint(f"Congrats you killed the {self.type}!", color="green")
                self.state = False
                break
        if self.state:
            player._take_damage(self.strength)