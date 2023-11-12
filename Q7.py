import random
count=0
for i in range(1,101):
    dice1= random.randint(1,6)
    dice2= random.randint(1,6)
    print(dice1,dice2)
    if dice1 == dice2:
        count=count+1
print(f"Out of hundred you rolled {count} doubles")




