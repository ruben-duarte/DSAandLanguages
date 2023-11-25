import random

def border(sentence, symbol):
    print(symbol*20)
    print(sentence)
    print(symbol*20)
    
def game_data():
    print()
    print("*"*20)
    print(f"{user_name} : {user_guess}")
    print(f"computer guess: {computer_guess}")
    print("*"*20)

user_guess = input("Ingresa papel, piedra o tijera: ").lower()
user_name = input("Ingresa tu nombre: ")
choices = ("piedra", "papel", "tijera")
computer_guess = random.choice(choices)
winner_user = (f"{user_name} gana!")

game_data()

#empate
if user_guess == computer_guess:
    print()
    border("Empate","=")

#tijera gana a papel
elif user_guess == "tijera":
    if computer_guess == "papel":
        print()
        
        border(winner_user, "*")
    else:
        print()
        border("gana pc","=")

#piedra gana a tijera
elif user_guess == "piedra":
    if computer_guess == "tijera":
        print()
        border(winner_user, "*")
    else:
        print()
        border("gana pc", "=")
#papel gana a piedra
elif user_guess == "papel":
    if computer_guess == "piedra":
     print()
     border(winner_user, "*")
    else:
        print()
        border("gana pc", "=")

