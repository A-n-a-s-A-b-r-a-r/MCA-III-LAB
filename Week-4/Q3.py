def square_list(lst):
    return [x**2 for x in lst]

lst = []
print("Enter Values of list (Enter Non-numeric value to end):")
while(True):
    i = input()
    if(i.isnumeric()):
        lst.append(int(i))
    else:
        break
print("Squared list:", square_list(lst))
