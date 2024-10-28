def create_even_split_lists():
    input_list = input("Enter distinct integers separated by spaces: ")
    integers = list(map(int, input_list.split()))

    if len(integers) % 2 != 0:
        print("The list must have an even number of elements.")
        return

    integers.sort()
    mid = len(integers) // 2

    L1 = integers[:mid]
    L2 = integers[mid:]  

    less_than_list = [x for x in L1 if x < L2[0]]
    greater_than_list = [x for x in L2 if x > L1[-1]]

    print("List 1 (L1):", less_than_list)
    print("List 2 (L2):", greater_than_list)

create_even_split_lists()
