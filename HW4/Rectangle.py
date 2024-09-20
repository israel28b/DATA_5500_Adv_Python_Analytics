class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width



def main():
    length=int(input("enter the length of the rectangle:"))
    width=int(input("enter the width of the rectangle:"))
    rect = Rectangle(length,width)
    print("the area of the rectangle is:",rect.area())


main()