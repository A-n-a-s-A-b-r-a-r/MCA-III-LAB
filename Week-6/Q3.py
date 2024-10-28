def sum_of_squares(num):
    if num<=9999 and num >= 1000:
        first_two = int(str(num)[:2])
        last_two = int(str(num)[-2:])
        return first_two**2 + last_two**2
    else:
        print("Enter 4 digit number")
        return 

number = int(input("Enter Number: "))
print("Sum of squares:", sum_of_squares(number))
