def count_occurrences(tpl, item):
    return tpl.count(item)

str = input("Enter a list of integers separated by spaces: ")
tpl = tuple(map(int, str.split()))
print("Number of occurrences of 50:", count_occurrences(tpl, 50))
