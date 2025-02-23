def game():
    return 5000

score = game()
with open("File IO/hiscore.txt") as f:
    hiscore = int(f.read())

if hiscore<score:
    with open("File IO/hiscore.txt","w") as f:
        f.write(str(score))
