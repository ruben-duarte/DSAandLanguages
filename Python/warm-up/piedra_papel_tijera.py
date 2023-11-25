user_guess = input("Ingresa papel, piedra o tijera: ").lower()
user_name = input("Ingresa tu nombre: ")
computer = "tijera"

#tijera gana a papel
if user_guess == "tijera":
    print("Empate")

#piedra gana a tijera
if user_guess == "piedra":
    print(f"{user_name} gana!")

#papel gana a piedra
if user_guess == "papel":
    print("Gana el pc")



