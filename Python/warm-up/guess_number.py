import random

welcome = """

     Bienvenido al juego! 🏓

"""
k= 10
i = 1
pc_prediction = random.randint(1,k)

def wrapper(title, symbol):
    print(symbol*80)
    print(title)
    print(symbol*80)
    print("="*80)
    return "Comencemos !"

intro = wrapper(welcome, '#')
print(intro)

def user_prompt():
    print()
    print("*"*30)
    user_number =input( f"Selecciona un número entre 1 y 10, para que la computadora intente adivinarlo.  Tu numero es : {pc_prediction}. Si es muy alto ingresa A,  muy bajo B, correcto C :  ").upper()
    return user_number

user_number = user_prompt()

while user_number != 'C':
    if user_number == 'A':
        k -= 1
       # print("k",k)
        pc_prediction = random.randint(i,k)
        user_number = user_prompt()
    elif user_number == 'B':
        i +=1
       # print("i",i)
        pc_prediction = random.randint(i,k)
        user_number = user_prompt()
if user_number == 'C':
    print()
    print("="*20)
    print(f" Tu numero es {pc_prediction}!")
    print()
    print("genial ", "✔" )
        


    


