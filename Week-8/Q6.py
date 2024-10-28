def find_max_vowel_in_file(file_path):
    vowels = 'aeiou'
    vowel_count = {v: 0 for v in vowels}

    try:
        with open(file_path, 'r') as file:
            content = file.read().lower() 

            for char in content:
                if char in vowels:
                    vowel_count[char] += 1

        max_vowel = max(vowel_count, key=vowel_count.get)
        return max_vowel, vowel_count[max_vowel]

    except FileNotFoundError:
        return "File not found."

file_path = input("Enter the file path: ")
max_vowel, count = find_max_vowel_in_file(file_path)
print(f"The vowel with the maximum instances is '{max_vowel}' with {count} occurrences.")
