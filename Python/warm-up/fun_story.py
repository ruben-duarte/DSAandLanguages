
def header():
    print("="*20)
    print("Fun story".center(15))
    print("="*20)
    return "welcome!"

title = header()
print(title)
print()

adjective = input("Adjective: ")
verb1 = input("first verb: ")
verb2 = input("second verb: ")
fav_color = input("color: ")
famous_name = input("name: ")

fun_story = f"computer programming is so {adjective} and it' so exciting because I like to {verb1}. Stay hydrated and {verb2}. Like you are {fav_color} {famous_name}."

print()
print(fun_story)

