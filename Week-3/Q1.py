def print_pattern(n):
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

print_pattern(int(input("Enter Number: ")))
