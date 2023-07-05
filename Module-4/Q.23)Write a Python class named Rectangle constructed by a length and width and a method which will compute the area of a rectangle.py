# 23.Write a Python class named Rectangle constructed by a length and
# width and a method which will compute the area of a rectangle

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
        my_rectangle = Rectangle(4, 5)
        print("The area of the rectangle is:", my_rectangle.area())