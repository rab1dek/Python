# 11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# Sample function : abs()
# Expected Result :
# abs(number) -> number
# Return the absolute value of the argument.

def doc(func):
    return func.__doc__

func = input("Write a name of function: ")
print(doc(func))