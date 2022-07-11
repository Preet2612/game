import random


def gameWin(comp, you):
    if comp == you:
        return None
    elif comp =='r':
        if you =='s':
            return False
        elif you =='p':
            return True
    elif comp =='p':
        if you =='r':
            return False
        elif you =='s':
            return True
    elif comp =='s':
        if you =='p':
            return False
        elif you =='r':
            return True


print("Comp Turn : Scissors(s) Paper(p) or Rock(r)?")
randNo =random.randint(1,3)
if randNo ==1:
    comp ='s'
elif randNo ==2:
    comp ='p'
elif randNo ==3:
    comp ='r'

you = input("PLayer 2 Turn : Scissors(s) Paper(p) or Rock(r)?")

a = gameWin(comp, you)

print(f"Computer Choose: {comp}")
print(f"You Choose: {you}")


if a==None:
    print("The game is tie!!!")
elif a:
    print("You win!!")
else:
    print("You lose!!")
