class Rectangle:

    def __init__(self,width,height):
        print("constructor called")
        self.width = width
        self.height = height

    def set_dimension(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return (self.width * self.height)
    
    def parimeter(self):
        return 2 * (self.width + self.height)

# rectangle1 = Rectangle()
# rectangle1.set_dimension(20,40)

# print("the width and height are ", rectangle1.width, rectangle1.height)
# print(rectangle1.width)
# print(rectangle1.height)
# print(rectangle1.area())
# print(rectangle1.parimeter())


w = int(input("Enter the width : "))
h = int(input("Enter the height : "))

rectangle2 = Rectangle(w,h)
# rectangle2.set_dimension(w,h)

print("the width and height are ", rectangle2.width, rectangle2.height)
print(rectangle2.width)
print(rectangle2.height)
print(rectangle2.area())
print(rectangle2.parimeter())