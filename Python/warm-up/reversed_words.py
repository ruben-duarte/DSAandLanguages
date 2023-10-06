phrase = " The greatest victory is the one that requires no battle"

def reverse_words(phrase):
    words = phrase.strip().split(" ")
    reversed_words = words[ : : -1]
    final_string = " ". join(reversed_words)
    return final_string

a = reverse_words(phrase)
print(a)
