import random
import time

#introducton

def introduction():
    print(""" You are in a land full of dragons. In front of you, you see two caves. \n
    In one cave, the dragon is friendly and will share his treasure with you. \n
    The other dragon is greedy and hungry, and will eat you on sight. """)

def choosecave():
    cave = ''
    while cave != "1" and cave != "2":
        cave = input("Wich cave will you choose?")
        print()
    return cave

def checkcave(choosencave):
    print("You approach the cave...")
    time.sleep(2)
    print("It is dark and spooky...")
    time.sleep(2)
    print("A large dragoon jumps, open the jaws and...")
    time.sleep(2)

    friendlycave = random.randint(1,2)

    if choosecave == str(friendlycave):
        print("...and it will give you a bunch of Bitcoins!")
    else:
        print("...and it will eat you you muther fucker!!!")

playagain = 'yes'

while playagain == 'yes' or playagain == 'y':
    introduction()
    caveNumber = choosecave()
    checkcave(choosecave)

    print('Do you want to play again? (yes or no)')
    playagain = input()

    