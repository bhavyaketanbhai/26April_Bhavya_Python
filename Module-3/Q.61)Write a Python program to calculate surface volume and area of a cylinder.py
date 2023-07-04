# 61.Write a Python program to calculate surface volume and area of a
# cylinder

import math

radius = 3
height = 5

surface_area = 2 * math.pi * radius * height + 2 * math.pi * radius ** 2
volume = math.pi * radius ** 2 * height

print(f"The surface area of the cylinder is {surface_area}.")
print(f"The volume of the cylinder is {volume}.")