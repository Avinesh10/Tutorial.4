hidden="6"
guess=input("Guess a number in between 1 and 20")
while guess !=hidden:
    if guess>hidden:
        print("Guess lower")
    elif guess<hidden:
        print("Guess higher")
    guess =input("Guess again")
    
if guess==hidden:
    print("You have guessed correctly")
    