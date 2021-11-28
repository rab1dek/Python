# 20. Write a Python program to get a string which is n (non-negative integer) copies of a given string.

def copies(n, txt):
    if n >= 1:
        for i in range (0, n):
            print(txt)
    else:
        print("Write a bigger number.")

txt = input("Write a text: ")
n = int(input("Write a numbers of copies: "))
copies(n, txt)