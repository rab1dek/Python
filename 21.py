# 21. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

def even_odd(n):
    if abs(n) % 2 == 0:
        print("Even")
    else:
        print("Odd")

n = int(input("Write a number: "))
even_odd(n)