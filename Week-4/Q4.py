list1 = input("Enter elements for List 1 separated by spaces: ").split()
list2 = input("Enter elements for List 2 separated by spaces: ").split()

min_length = min(len(list1), len(list2))

for i in range(min_length):
    print(f"{list1[i]}, {list2[-(i+1)]}")
