# This is an example of a class inheritance #

class Polygon: # This class acts as the Parent Object
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = []
        for i in range(no_of_sides):
            self.sides.append(0)

    def input_sides(self):
        for i in range(self.n):
            self.sides[i] = float(input(f"Enter side {i+1}: "))

    def display_sides(self):
        for i in range(self.n):
            print(f"Side {i+1} is {self.sides[i]}")

class Triangle(Polygon): # This is a subclass which inherents the Polygon Class
    def __init__(self):
        Polygon.__init__(self, 3) # This will allow us to call on the Polygon instantiation, and pass value to the Polygon class
    # With this it will allow us to access the functions/methods created in the Parent Class. Basically inheriting its traits.

    def find_area(self):
        a, b, c = self.sides

        semi_perimeter = (a + b + c) / 2
        sp = semi_perimeter
        triangle_area = (sp*(sp-a)*(sp-b)*(sp-c)) ** 0.5
        
        print(f"The area of the triangle is {triangle_area}")

class Square(Polygon):
    def __init__(self):
        Polygon.__init__(self, 4)

    def find_area(self):
        a, b, c, d = self.sides

        semi_perimeter = (a + b + c + d) / 2
        s = semi_perimeter
        square_area = (s*(s-a)*(s-b)*(s-c)*(s-d)) ** 0.5

        print(f"The are of the square is {square_area}")

t = Triangle() # We create an instance object to call the Triangle class to the Base Class
t.input_sides() 
t.display_sides() 
t.find_area()