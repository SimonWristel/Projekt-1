import random
import os
from colors import bcolors

os.system('cls')

print(bcolors.CYAN + """ 
 _______________________
|-----------------------|
|----- GISSA TALET -----|
|----DU HAR 7 FÖRSÖK----|
|-----------------------|
|_______________________|\n\n""")
    
random_number = random.randint(1,100)
guesses = 0

while guesses <= 7:
    try:
        guess = int(input(bcolors.GREEN + "Gissa det hemliga talet: "))
    except ValueError: 
        print(bcolors.RED + "Du måste skriva siffror och inga bokstäver!!")
        continue

    guesses += 1

    if guess > random_number:
        print(bcolors.BLUE + "För högt, skriv lägre tal")

    elif guess < random_number:
        print(bcolors.YELLOW + "För lågt, skriv ett högre tal")
        
    elif guess == random_number:
        print(bcolors.PURPLE + f'\nGrattis du har hittat talet {random_number} på {guesses} försök!\n\n')
        break
        
    if guesses == 7:
        print(bcolors.RED + bcolors.BLUE + f'\nTyvärr, du hittade inte det hemliga talet: {random_number}.')
        break
    
        