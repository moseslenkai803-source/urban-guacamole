class Shape:
    def __init__(self, shape_name):
        self.shape_name = shape_name

    def describe(self):
        print(f"This is a {self.shape_name}.")

    def display_info(self):
        print("--------------------------------")
        print(f"shape: {self.shape_name}")
        print(f"area: {self.area()}")
        print(f"perimeter: {self.perimeter()}")
        print("--------------------------------")

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(shape_name="Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        self.shape_name = "Square"

s1 = Square(length=10)
print("Shape name is ", s1.shape_name)
print("Area is ", s1.area())
print("Perimeter is ", s1.perimeter())
s1.display_info()
s1.describe()