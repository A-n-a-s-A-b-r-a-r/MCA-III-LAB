def cal_sum_sub(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction

a = int(input("Enter First number: "))
b = int(input("Enter Second number: "))
result = cal_sum_sub(a, b)
print("Addition:", result[0], "Subtraction:", result[1])
