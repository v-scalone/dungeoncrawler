from random import randrange, choice
from visual import tprint
from monster import Monster
from player import Player


class Room:
    def __init__(self, monster_prob=3, chest_prob=5):
        self.monster_prob = monster_prob
        self.chest_prob = chest_prob

    def enter(self, player):
        if not randrange(self.monster_prob):  # truthy when randrange chose 0
            type = choice(("slime", "skeleton", "ghost"))
            monster = Monster(
                type,
                hp=randrange(
                    2, 6),
                strength=randrange(
                    1, 5))
            tprint(
                f"OH NO!\nA {monster.type}, with {monster.hp} HP and {monster.strength} strength guards this room!",
                "red")
            while True:
                tprint(
                    "What do you want to do?\n[r]un or [f]ight?",
                    color="magenta")
                action = input()
                if action.lower() == "r":
                    tprint(
                        "You have a one in three chance of fleeing this monster.",
                        color="magenta")
                    if not randrange(3):  # truthy when randrange chose 0
                        tprint(
                            "Congrats! You managed to escape!",
                            color="green")
                    else:
                        tprint(f"You failed to run away.", color="red")
                        player.take_damage(monster.strength)
                    break
                elif action.lower() == "f" or action == "f":
                    player.fight(monster)
                    break
                else:
                    tprint("Please make a vaild choice!", color="magenta")


if __name__ == "__main__":
    room = Room()
    p = Player("vic")
    room.enter(p)
