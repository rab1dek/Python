# 22. Write a Python program to count the number 4 in a given list.

def count4(list):
    c = 0
    for number in list:
        if number == '4':
            c += 1
    return c

str_list = input("Write a list of number with commas: ")
list = str_list.split(',')
print(count4(list))