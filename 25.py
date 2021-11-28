# 25. Write a Python program to check whether a specified value is contained in a group of values. Go to the editor
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

list = [1, 5, 8, 3]

def check(number):
    for num in list:
        if number == num:
            return True
    return False

number = int(input("Write a number: "))
print(check(number))