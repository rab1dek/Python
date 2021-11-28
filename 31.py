# 31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

def gcd(a, b):
    while (a != b):
        if a > b:
            a -= b
        else:
            b -= a
    return a

print(gcd(336,360))