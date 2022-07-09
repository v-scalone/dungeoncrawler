from visual import tprint


class Monster:
    def __init__(self, type, hp, strength):
        self.type = type
        self.hp = hp
        self._alive = True
        self.strength = strength

    def hit(self, player, amount):
        while self._alive:
            for i in range(amount):
                if self.hp > amount:
                    self.hp -= 1
                else:
                    tprint(
                        f"Congrats you killed the {self.type}!",
                        color="green")
                    self._alive = False
                    break
            if self._alive:
                tprint(
                    f"The Monster took a hit!\nIt's remaining HP is {self.hp}.",
                    color="blue")
                player.take_damage(self.strength)
