def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

number = int(input("Enter Number: "))
print("Factorial of", number, "is", factorial(number))
