def reverse_digits(num):
    while num > 0:
        digit = num % 10
        print(digit, end="")
        num = num // 10

number = int(input("Enter Number: "))
reverse_digits(number)
