def print_divisible_by_5(numbers):
    for number in numbers:
        if number % 5 == 0:
            print(number)

numbers = [int(input(f"Enter number {i+1}: ")) for i in range(20)]
print("Numbers divisible by 5:")
print_divisible_by_5(numbers)
