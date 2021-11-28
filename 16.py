# 16. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference

def check(number):
    if number > 17:
        return (number - 17) * 2
    else:
        return abs(17 - number)

number = int(input("Write a number: "))
print(check(number))