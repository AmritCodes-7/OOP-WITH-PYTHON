import random


def game(a, b):
    if comp == "r" and you == "p":
        return True
    elif comp == "p" and you == "r":
        return False
    elif comp == "s" and you == "r":
        return True
    elif comp == "r" and you == "s":
        return False
    elif comp == "p" and you == "s":
        return True
    elif comp == "s" and you == "p":
        return False
    else:
        return None


print("COMPUTER Turn: ROCK(r), PAPER(p) or SCISSORS(s)?")
randno = random.randint(1, 3)

if randno == 1:
    comp = "r"
elif randno == 2:
    comp = "s"
else:
    comp = "p"

you = input("PLAYER's Turn: ROCK(r), PAPER(p) or SCISSORS(s)?")
res = game(comp, you)
print("comp: ", comp)
if res:
    print("You win")
elif res == None:
    print("Draw")
else:
    print("you loose")
