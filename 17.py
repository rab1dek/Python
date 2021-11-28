# 17. Write a Python program to test whether a number is within 100 of 1000 or 2000.

def check(n):
    if abs(n - 1000) <= 100 or abs(n - 2000) <= 100:
        return True
    else:
        return False

print(check(1000))
print(check(900))
print(check(800))
print(check(2200))
print(check(2050))
print(check(-2050))