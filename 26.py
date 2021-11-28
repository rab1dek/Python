# 26. Write a Python program to create a histogram from a given list of integers.

list = [3,6,1,3]
def histogram():
    for num in list:
        print(str(num) + "\t", end = '')
        for i in range(0,num):
            print("*", end = '')
        print("\n")

histogram()