def max_alphabet_instances(file_path):
    with open(file_path, 'r') as file:
        content = file.read().lower()

    alphabet_count = {}
    for char in content:
        if char.isalpha():
            alphabet_count[char] = alphabet_count.get(char, 0) + 1

    max_count = max(alphabet_count.values())
    max_alphabets = [char for char, count in alphabet_count.items() if count == max_count]

    return max_alphabets, max_count

# Example usage
print(max_alphabet_instances('Week-9/file.txt'))
