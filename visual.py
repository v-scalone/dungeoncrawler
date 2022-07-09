from termcolor import cprint
from time import sleep


def tprint(string, color="grey"):
    for x in string:
        cprint(x, color, end="", flush=True)
        sleep(0.06)
    print("")
