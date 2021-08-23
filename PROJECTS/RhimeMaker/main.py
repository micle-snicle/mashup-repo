"""
This funny program will create the poem based on
random words from the list and rhimes sending API calls to datamuse.
Structure:

Ask user for a name
load a random word from each list by calling a separete functions
    sebd generated word to API and get rhime
    place rhime in an predefined sentences.
"""


import random
import requests
import time

user_name = input("What is your name? ")
print()
print(f"Entered name is {user_name}. Let the fun begin!")

for i in range(0, 5):
    print("----- WORKING HARD -----")
    time.sleep(0.5)


    

