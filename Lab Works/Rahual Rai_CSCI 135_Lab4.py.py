# Question 1:

# creating a class to calculate and print out the area of a circle
class Circle:

    # initialize class attribute
    pi = 3.14

    # initialize instance attribute
    def __init__(self, radius):
        self.radius = radius

    # class method to calculate and print the area of a circle
    def area(self):
        area_circ = self.pi * self.radius**2
        print("Area of circle: ", area_circ)

# instantiating the Circle class to the variable c1 with a radius of 10 unit
c1 = Circle(10) 

# calling the area method to calculate and print out the area of a circle
c1.area() 

#Output: Area of circle:  314.0





# question 2:

# creating a class to calculate and print out the area of a rectangle
class Rectangle:

    # initialize instance attributes
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # class method to calculate and print the area of a rectangle
    def area(self):
        area_rect = self.length * self.width
        print("Area of rectangle: ", area_rect)
    


# instantiating the Rectangle class to the variable r1 with a length of 10 unit and width of 9 unit
r1 = Rectangle(10, 9) 

# calling the area method to calculate and print out the area of a rectangle
r1.area()

#Output: Area of rectangle:  90