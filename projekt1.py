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
    
secret_number = random.randint(1,100)
total_guesses = 0

while total_guesses <= 7:
    try:
        guess = int(input(bcolors.GREEN + "Gissa det hemliga talet: "))
    except ValueError: 
        print(bcolors.RED + "Du måste skriva siffror och inga bokstäver!!")
        continue

    total_guesses += 1

    if guess > secret_number:
        print("För högt, skriv lägre tal")

    elif guess < secret_number:
        print(bcolors.YELLOW + "För lågt, skriv ett högre tal")
        
    elif guess == secret_number:
        print(bcolors.PURPLE + f'\nGrattis du har hittat talet! {secret_number} på  + {total_guesses} försök!\n\n')
        break
        
    if total_guesses == 7:
        print(bcolors.UNDERLINE + bcolors.BLUE + f'\nTyvärr, du hittade inte det hemliga talet: {secret_number}.')
        break
    
        