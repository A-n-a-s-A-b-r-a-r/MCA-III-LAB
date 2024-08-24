def count_digits(num):
    count = 0
    while num != 0:
        num = num // 10
        count += 1
    return count

number =  int(input("Enter Number: "))
print("Total number of digits:", count_digits(number))
