def game():
    return 30


score = game()
with open("D:\\2024\\for python\\10 FILE IO\\highscore.txt") as f:
    highscore = f.read()

if highscore == "":
    with open("D:\\2024\\for python\\10 FILE IO\\highscore.txt", "w") as f:
        f.write(str(score))

elif int(highscore) < score:
    with open("D:\\2024\\for python\\10 FILE IO\\highscore.txt", "w") as f:
        f.write(str(score))
