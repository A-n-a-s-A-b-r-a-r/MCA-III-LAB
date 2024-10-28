def create_phonebook():
    phonebook = {}
    phonebook["Alice"] = "123-456-7890"
    phonebook["Bob"] = "234-567-8901"
    phonebook["Charlie"] = "345-678-9012"
    return phonebook

def get_phone_number(phonebook, name):
    return phonebook.get(name, "Name not found")

phonebook = create_phonebook()
name = input("Enter a name: ")
print("Phone number:", get_phone_number(phonebook, name))
