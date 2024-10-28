def get_distinct_even_integers():
    while True:
        user_input = input("Enter distinct integers separated by spaces: ")
        integer_list = list(map(int, user_input.split()))
        distinct_integers = list(set(integer_list))

        if len(distinct_integers) % 2 == 0:
            return distinct_integers
        else:
            print("Please enter an even number of distinct integers.")

def create_lists(original_list):
    mid_index = len(original_list) // 2
    list1 = []
    list2 = []

    for i in range(mid_index):
        list1.append(original_list[i])
        list2.append(original_list[mid_index + i])

    return list1, list2

original_list = get_distinct_even_integers()
list1, list2 = create_lists(original_list)

print("Original List:", original_list)
print("List 1 (elements less than List 2):", list1)
print("List 2:", list2)
