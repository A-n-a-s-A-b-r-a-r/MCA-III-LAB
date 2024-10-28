def encrypt_string(main_str, symbol_str):
    encrypted = ''.join([char + symbol_str for char in main_str])
    return encrypted

def decrypt_string(encrypted_str, symbol_str):
    return encrypted_str.replace(symbol_str, '')

main_str = input("Enter a String: ")
symbol_str = input("Enter symbol: ")
encrypted = encrypt_string(main_str, symbol_str)
print("Encrypted string:", encrypted)
decrypted = decrypt_string(encrypted, symbol_str)
print("Decrypted string:", decrypted)
