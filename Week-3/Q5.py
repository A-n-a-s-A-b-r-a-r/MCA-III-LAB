def remove_chars(s, n):
    return s[:n]

string = input("Enter Number: ")
n = int(input("Enter index: "))
print("New string:", remove_chars(string, n))
