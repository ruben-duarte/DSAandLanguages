word = "secret"

allowed_errors = 5
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end='  ')
        else:
            print('__', end='  ')
    print() 
    print()

    guess = input(f"Allowed errors {allowed_errors}.  write next guess: ")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        allowed_errors -= 1
        if allowed_errors == 0:
            break

    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done:
    print(f"You found the word! it was {word}")
else:
    print(f"Game over! It was {word}")



