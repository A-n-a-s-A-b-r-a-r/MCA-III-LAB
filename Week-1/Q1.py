def product_or_sum(a, b):
    product = a * b
    if product <= 5000:
        print("Sum: ",end="")
        return a + b
    print("Product: ",end="")
    return product

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = product_or_sum(num1, num2)
print(result)
