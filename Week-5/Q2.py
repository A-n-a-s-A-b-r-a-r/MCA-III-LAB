import random

def random_char_from_string(s):
    return random.choice(s)

user_string = input("Enter a string: ")
print("Random character:", random_char_from_string(user_string))
