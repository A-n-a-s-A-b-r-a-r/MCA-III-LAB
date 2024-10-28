def separate_numbers_and_alphabets(input_string):
    L1 = []  
    L2 = []  

    for char in input_string:
        if char.isdigit():
            L1.append(char)
        elif char.isalpha():
            L2.append(char)

    return L1, L2

input_string = input("Enter a string containing alphabets and numbers: ")
numbers, alphabets = separate_numbers_and_alphabets(input_string)
print("List of Numbers (L1):", numbers)
print("List of Alphabets (L2):", alphabets)
