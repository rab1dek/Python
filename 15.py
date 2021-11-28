# 15. Write a Python program to get the volume of a sphere with radius 6.
import math

def calc_volume_sphere(radius):
    V = 4/3 * math.pi * pow(radius, 3)
    return V

radius = 6
print(calc_volume_sphere(radius))