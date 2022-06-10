import random
#Snake Water Gun or Rock Paper Scissors
def gameWin(comp, you):
    #if two value are equal, declare tie
    if comp == you:
        return None
    #check all possibilities when computer choose S
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
             #check all possibilities when computer choose W
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
             #check all possibilities when computer choose G
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True
print("Comp Turn: Snake(s) Water(w) Gun(G)")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("your Turn: Snake(s) Water(w) Gun(G)")
a=gameWin(comp, you)

print(f"computer choose {comp}")
print(f"you choose {you}")
if a== None:
    print("The game is a tie!")

elif a:
    print("you Win!")

else:
    print("you loose")