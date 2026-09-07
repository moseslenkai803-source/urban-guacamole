class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
        self.shape_name="Rectangle"

    def area(self):
        area=self.length*self.width
        print(f"For {self.shape_name} of length {self.length} and width {self.width}, area: {area}")

class Square:
    def __init__(self,length):
        self.length=length
        self.width=length
        self.shape_name="Square"

    def area(self):
        area=self.length*self.width
        print(f"For {self.shape_name} of length {self.length} and width {self.width}, area: {area}")

r1=Rectangle(length=20,width=10)
r1.area()   
print(r1.shape_name)

s1=Square(length=10)
s1.area()
print(s1.shape_name)