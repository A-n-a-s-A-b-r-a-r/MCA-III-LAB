def char_counts(s):
    uppercase = sum(1 for c in s if c.isupper())
    lowercase = sum(1 for c in s if c.islower())
    alphabets = sum(1 for c in s if c.isalpha())
    digits = sum(1 for c in s if c.isdigit())
    return uppercase, lowercase, alphabets, digits

s = input("Enter a string: ")
uppercase, lowercase, alphabets, digits = char_counts(s)
print("Uppercase characters:", uppercase)
print("Lowercase characters:", lowercase)
print("Total alphabets:", alphabets)
print("Digits:", digits)
