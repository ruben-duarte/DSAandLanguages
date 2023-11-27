import random

def border(sentence, symbol):
    print(symbol*20)
    print(sentence)
    print(symbol*20)
    
def game_data():
    print()
    print("="*20)
    print(f"{user_name} : {user_guess}, number of wins: {user_wins}")
    print(f"computer guess: {computer_guess}, number of wins: {computer_wins}")
    print("="*20)


choices = ("piedra", "papel", "tijera")
rounds = 1
user_wins = 0
computer_wins = 0

while True:
    print("*"*20)
    print(f"Round  : {rounds} ")
    print("*"*20)
    user_guess = input("Ingresa papel, piedra o tijera: ").lower()
    user_name = input("Ingresa tu nombre: ")

    computer_guess = random.choice(choices)
    winner_user = (f"{user_name} gana!")

    if user_guess not in choices:
        print("Ingrese una opción válida. Intente de nuevo")
        continue   
    else:

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
                user_wins += 1
            else:
                print()
                border("gana pc","=")
                computer_wins += 1

        #piedra gana a tijera
        elif user_guess == "piedra":
            if computer_guess == "tijera":
                print()
                border(winner_user, "*")
                user_wins += 1
            else:
                print()
                border("gana pc", "=")
                computer_wins += 1
        #papel gana a piedra
        elif user_guess == "papel":
            if computer_guess == "piedra":
                print()
                border(winner_user, "*")
                user_wins += 1
            else:
                print()
                border("gana pc", "=")
                computer_wins += 1

    rounds += 1

    if user_wins == 2 or computer_wins == 2:
        break