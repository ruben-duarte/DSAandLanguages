import sys 
import random

min_number = int(sys.argv[1])
max_number = int(sys.argv[2])

target_number = random.randint(min_number, max_number)

while True:
    print("="*30)
    user_guess =int(input(f"Guess a number between {min_number} and {max_number} : "))
    if user_guess == target_number:
        print(f" You won !  the number was {target_number}")
        break
    else:
        print("try again ")
