#In this chapter, you’re going to make a
#Guess the Number game. The computer
#will think of a secret number from 1 to 20
#and ask the user to guess it. After each guess,
#the computer will tell the user whether the number is
#too high or too low. The user wins if they can guess
#the number within six tries.

import random

myname = input("Hi! This is a guessing game. What is your Name?")
print("Great {}, nice to meet you.".format(myname))


def randomguess():
    randomnumber = random.randint(0, 20)
    return randomnumber
randomnumber = randomguess()


def corectguess(randomnumber):
    #guesstaken = 0
    for i in range(6):
        myguess = int(input("Okay {}, please guess the number from 0 to 20. Now.".format(myname)))

        if myguess < randomnumber:
            print("No, {} is too low. Try again.".format(myguess))
        
        elif myguess > randomnumber:
            print("No, {} is too high. Try again.".format(myguess))

        elif myguess == randomnumber:
            print("Great, your guess {} is a correct number!".format(myguess))
            print("Therefore a correct number is {}.".format(randomnumber))
            print("You needed exactly {} guesses to guess my number. Not bad!".format(i))
            break
    if myguess != randomnumber: 
            print("No, you ran out of tries!. Number I was looking at was {}.".format(randomnumber))     
            
corectguess(randomguess())
