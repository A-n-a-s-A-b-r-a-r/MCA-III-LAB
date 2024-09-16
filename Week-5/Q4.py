def merge_odd_even(list1, list2):
    new_list = [x for x in list1 if x % 2 != 0]
    new_list.extend([x for x in list2 if x % 2 == 0])
    return new_list

n = int(input("Enter size of list: "))
print("Enter elements of First list \n")
list1 = [int(input()) for x in range(n)]

print("Enter elements of Second list \n")
list2 = [int(input()) for x in range(n)]

print("Merged list:", merge_odd_even(list1, list2))
