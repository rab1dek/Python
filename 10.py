# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5
# Expected Result : 615

def calc(n):
    return n + n*n + n*n*n

def compute(n):
    second = int("%s%s"% (n, n))
    third = int("%s%s%s"% (n, n, n))
    return n + second + third

n = int(input("Write a integer: "))
print(calc(n))
print(compute(n))