def replace_max_word(file_path):
    with open(file_path, 'r') as file:
        content = file.read().lower()
    
    word_count = {}
    words = content.split()
    
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    max_word = max(word_count, key=word_count.get)
    print(f"Most frequent word: {max_word} (occurrences: {word_count[max_word]})")
    
    updated_content = content.replace(max_word, 'Aligarh')
    
    with open('updated_file.txt', 'w') as file:
        file.write(updated_content)

# Example usage
replace_max_word('Week-10/example.txt')
