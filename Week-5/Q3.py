import random
import string

def generate_password():
    password = []
    password.extend(random.choices(string.ascii_uppercase, k=2))
    password.extend(random.choices(string.digits, k=1))
    password.extend(random.choices(string.punctuation, k=1))
    password.extend(random.choices(string.ascii_letters + string.digits + string.punctuation, k=6))
    random.shuffle(password)
    return ''.join(password)

print("Random Password:", generate_password())
