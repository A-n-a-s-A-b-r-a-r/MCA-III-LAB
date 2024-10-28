def find_max_vowel_instances(file_path):
    vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    try:
        with open(file_path, 'r') as file:
            content = file.read().lower()  

            for char in content:
                if char in vowel_counts:
                    vowel_counts[char] += 1

        max_vowel = max(vowel_counts, key=vowel_counts.get)
        max_count = vowel_counts[max_vowel]

        return max_vowel, max_count

    except FileNotFoundError:
        return "File not found. Please check the file path." 
    except Exception as e:
        return f"An error occurred: {e}"

file_path = input("Enter the path of the file: ")
result = find_max_vowel_instances(file_path)

if isinstance(result, tuple):
    max_vowel, max_count = result
    print(f"The vowel with the maximum instances is '{max_vowel}' with {max_count} occurrences.")
else:
    print(result)
