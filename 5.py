# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
def reverse(txt):
    return txt[::-1]

first_name = input("Write your first name: ")
last_name = input("Write your last name: ")

print("Reverse: ")
print(reverse(first_name) + " " + reverse(last_name))
print(last_name + " " + first_name)