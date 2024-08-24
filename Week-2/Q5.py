def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num = num // 10
    return total

number = int(input("Enter Number: "))
print("Sum of digits:", sum_of_digits(number))
