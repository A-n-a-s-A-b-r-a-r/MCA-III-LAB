def concatenate_tuples(tup1, tup2):
    return tup1 + tup2

tup1 = tuple(input("Enter Elements of first tuple: ").split())
tup2 = tuple(input("Enter Elements of first tuple: ").split())
tup3 = concatenate_tuples(tup1, tup2)
print(tup3)
