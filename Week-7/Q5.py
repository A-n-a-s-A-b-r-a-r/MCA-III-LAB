def separate_alphabets_and_numbers(input_string):
    L1 = []  
    L2 = []  
    for char in input_string:
        if char.isdigit(): 
            L1.append(char)
        elif char.isalpha():  
            L2.append(char)

    return L1, L2

input_string = input("Enter a string containing alphabets and numbers: ")
numbers_list, alphabets_list = separate_alphabets_and_numbers(input_string)

print("List of numbers (L1):", numbers_list)
print("List of alphabets (L2):", alphabets_list)
