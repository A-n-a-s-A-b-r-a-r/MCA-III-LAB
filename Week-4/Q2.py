def is_first_last_same(lst):
    if lst[0] == lst[-1]:
        return True
    return False

lst = []
print("Enter Values of list (Enter Non-numeric value to end):")
while(True):
    i = input()
    if(i.isnumeric()):
        lst.append(int(i))
    else:
        break
print("First and last are the same:", is_first_last_same(lst))
