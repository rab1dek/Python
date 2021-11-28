# 32. Write a Python program to get the least common multiple (LCM) of two positive integers

def gcd(a, b):
    while (a != b):
        if a > b:
            a -= b
        else:
            b -= a
    return a

def lcm(a, b):
    return (a*b)/gcd(a,b)

print(lcm(14,51))