# 23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string.
# Return the n copies of the whole string if the length is less than 2.

def copies(n, txt):
    result = ""
    if len(txt) <= 2:
        for i in range (0,n):
            result += txt
        return txt + result
    else:
        for i in range (0,n):
            result += txt[:2]
        return txt + result

txt = "Pomidorek"
txt2 = "Ka"
n = 5
print(copies(n, txt))
print(copies(n, txt2))
