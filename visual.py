from termcolor import cprint
from time import sleep
import sys


def tprint(string, color="grey"):
    for x in string:
        cprint(x, color, end="")
        sys.stdout.flush()
        sleep(0.06)
    print("")
