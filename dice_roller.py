'''The objective is to develop a dice roller with a 
faux graphical output of the die in ascii graphics.
You should get a randomly generated number from 1-6 each time.
It should also offer you the option to roll the doce again.'''

from random import randint

#drawing the dice to call later
def dice1():
    print("[-------]")
    print("[       ]")
    print("[   0   ]")
    print("[       ]")
    print("[-------]")

def dice2():
    print("[-------]")
    print("[0      ]")
    print("[       ]")
    print("[      0]")
    print("[-------]")

def dice3():
    print("[-------]")
    print("[0      ]")
    print("[   0   ]")
    print("[      0]")
    print("[-------]")

def dice4():
    print("[-------]")
    print("[0     0]")
    print("[       ]")
    print("[0     0]")
    print("[-------]")

def dice5():
    print("[-------]")
    print("[0     0]")
    print("[   0   ]")
    print("[0     0]")
    print("[-------]")

def dice6():
    print("[-------]")
    print("[0  0  0]")
    print("[0  0  0]")
    print("[0  0  0]")
    print("[-------]")

def roll_dice():
    roll_dice = True
    while roll_dice == True:
        print("Rolling....")
        chosen_die = randint(1,6)
        if chosen_die == 1:
            dice1()
        elif chosen_die == 2:
            dice2()
        elif chosen_die == 3:
            dice3()
        elif chosen_die == 4:
            dice4()
        elif chosen_die == 5:
            dice5()
        else:
            dice6()
        print("Do you want to roll again? Press Y to roll again or any other key to exit.")
        choice = input()
        if choice == str("Y") or choice == str("y"):
            roll_dice = True
        else:
            roll_dice = False
            print("Goodbye!")
            break


roll_dice()
        