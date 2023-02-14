1)Animal Inheritance: Create a base class "Animal" with an attribute "name" and a method "speak".
 Create two subclasses "Dog" and "Cat" that inherit from "Animal"
 and implement the "speak" method to make a sound specific to each animal.

class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError()

class Dog (Animal):
    def speak(self):
        return self.name + " Woof"

class Cat(Animal):
    def speak(self):
        return self.name + " Meow"


D = Dog ("Doggy says ")
C = Cat ("Kitty says ")
print(D.speak())
print(C.speak())


2)Vehicle Inheritance: Create a base class "Vehicle" with an attribute "num_of_wheels" 
and a method "drive". Create two subclasses "Car" and "Bicycle" that inherit from "Vehicle"
 and implement the "drive" method in a way that makes sense for each vehicle.

class Vehicle():
    def __init__(self,num_of_wheels):
        self.num_of_wheels = num_of_wheels


    def drive (self):
        print("My vehicle has", self.num_of_wheels, "wheels")

class Car (Vehicle):
    def __init__(self, color, brand, num_of_wheels):
        super().__init__(num_of_wheels)
        self.color = color
        self.brand = brand
    def drive(self):
        print("I am driving",self.color, self.brand,"that has", self.num_of_wheels, " wheels" )

v = Vehicle(4)
c = Car("Black", "BMW", 4 )
v.drive()
c.drive()

class Bicycle(Vehicle):
    def __init__(self,type):
        super().__init__(num_of_wheels=2)
        self.type = type

    def drive(self):
        print("My bike has ", self.num_of_wheels ,"wheels and it is", self.type)

b = Bicycle("Road type of bike")
b.drive()



3)Shape Inheritance: Create a base class "Shape" with an attribute "num_of_sides" and a method "area".
Create two subclasses "Triangle" and "Rectangle" that inherit from "Shape" 
and calculate the area of the shape using the values provided.

class Shape:
    def __init__(self):
        pass
    def area(self):
        print("returns the area the shape")


class Rectangle(Shape):
    def __init__(self,side1, side2):
        super().__init__()
        self.side1 = side1
        self.side2 = side2

    def area(self):
        return (self.side1 * self.side2)

rec = Rectangle(4,10)
print("The area of rectangle is:" ,rec.area())

class Triangle(Rectangle,Shape):
    # def __init__(self,side1,side2):
    #     # Shape.__init__(self,side)
    #     # Rectangle.__init__(self,side1)
    #     super().__init__(side1,side2)
    def area(self):
        return round(self.side1 * self.side2 / 2)

t = Triangle(5,6)
print("The are of triangle is :" , t.area())
