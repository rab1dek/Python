# 30. Write a Python program that will accept the base and height of a triangle and compute the area.

def triangle_area(a, h):
    return (a*h)/2

a = int(input("Write the base of a triangle: "))
h = int(input("Write the height of a triangle: "))
print(triangle_area(a, h))