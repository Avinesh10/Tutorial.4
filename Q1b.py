import random
hidden= 6
while True:
    guess=random.randint(1,20)
    print(guess , " is not the correct guess")
    if guess == hidden:
        print(f"{guess} is the correct guess ")
        break
    