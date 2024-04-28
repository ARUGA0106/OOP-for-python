"""
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length * self.width
length  = 8
width = 4

obj = Rectangle(length, width)
print(f"The area of rectangle is: {obj.area()}")


from math import pi

class Circle:
    def __init__(self,radius):
         self.radius=radius

    def area(self):
          return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius

    # creating an instance of the circle class with radius 21cm
my_circle = Circle(21)
    # computing area and perimeter of the circle
area = my_circle.area()
perimeter = my_circle.perimeter()

    # print the results
print(" The area of the circle is:", area,"square cm")
print("The perimeter of the circle is:",perimeter,"cm")

class Sum:
    num1 = eval(input("enter the first number"))
    num2 = eval(input("enter the second number"))

    Sum = num1 + num2
    print("the sum of the numbers is:",Sum)


class Sum:
    def add(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        return self.num1 + self.num2

a = eval(input("enter the first number:"))
b = eval(input("enter the second number:"))

obj = Sum()
print(f"the sum of {a} and {b} is {obj.add(a,b)}:")



#using constructor
class Sum:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2

a = eval(input("enter the first number:"))
b = eval(input("enter the second number:"))

obj = Sum(a,b)
print(f"the sum of {a} and {b} is {obj.add()}")


import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2*math.pi*self.radius


a = eval(input("please enter the value of the radius"))
obj = Circle(a)
print(f"The area of the circle for radius {a} is {obj.area()} while the perimeter is {obj.perimeter()}")
#for limited no of decimal point
print("the area is %.3f and the perimeter is %.2f" % (obj.area(), obj.perimeter()))

#checking if object is the MUST in oop
class Dit:
    txt = " Dit is the best place to be"

print(Dit().txt)
#....OBJECT IS NOT MUST.....

#checking which no is greater than the other
class Check:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def checkMethod(self):
        if(self.a > self.b):
            print(f"{self.a} is greater than {self.b}")
        else:
            print(f"{self.b} is greater than {self.a}")


num1 = eval(input("please enter the first number:"))
num2 = eval(input("please enter the second number:"))

Check(num1, num2).checkMethod()

#with object creation
class Check:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def checkMethod(self):
        if(self.a > self.b):
            print(f"{self.a} is greater than {self.b}")
        else:
            print(f"{self.b} is greater than {self.a}")


num1 = eval(input("please enter the first number:"))
num2 = eval(input("please enter the second number:"))

obj = Check(num1, num2)
obj.checkMethod()



#INHERITANCE(SINGLE)

class Rectangle:
    def __init__(self,w,l):
        self.w = w
        self.l = l

class Area(Rectangle):
    def area(self):
        return self.w * self.l

width = 12
length = 10

obj = Area(width,length)
print("the area is: ",obj.area())


class Sum:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

class findsum(Sum):
    def add(self):
        return self.num1 + self.num2

a = eval(input("please enter first number"))
b = eval(input("please enter the second number"))

obj = findsum(a, b)

print(f"the sum of {a} and {b} is {obj.add()}")

#OVERRIDING
class Sum:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

class findsum(Sum):
    def __init__(self, num1, num2): # overide the init above
       Sum.__init__(self,num1,num2)
    def add(self):
        return self.num1 + self.num2

a = eval(input("please enter first number"))
b = eval(input("please enter the second number"))

obj = findsum(a, b)

print(f"the sum of {a} and {b} is {obj.add()}")


#EXTEND CONCEPT*******

class Sum:
    def __init__(self,num1):
        self.num1 = num1


class findsum(Sum):
    def __init__(self, num2):
        self.num2 =num2
       Sum.__init__(self,num1)
    def add(self):
        return self.num1 + self.num2

a = eval(input("please enter first number"))
b = eval(input("please enter the second number"))

obj = findsum(a, b)

print(f"the sum of {a} and {b} is {obj.add()}")



class Sum:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

class findsum(Sum):
    def __init__(self, num1, num2): # overide the init above
       Sum.__init__(self,num1,num2)
    def add(self):
        return self.num1 + self.num2

a = eval(input("please enter first number"))
b = eval(input("please enter the second number"))

obj = findsum(a, b)

print(f"the sum of {a} and {b} is {obj.add()}")

lass Sum:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

class findsum(Sum):
    def __init__(self, num1, num2): # overide the init above
       Sum.__init__(self,num1,num2)
    def add(self):
        return self.num1 + self.num2

a = eval(input("please enter first number"))
b = eval(input("please enter the second number"))

obj = findsum(a, b)

print(f"the sum of {a} and {b} is {obj.add()}")


class Sum:
    def __init__(self,num1):
        self.num1 = num1


class findsum(Sum):
    def __init__(self, num1, num2): # overide the init above
       super().__init__(num1)
    def add(self):
        return self.num1 + self.num2

a = eval(input("please enter first number"))
b = eval(input("please enter the second number"))

obj = findsum(a, b)

print(f"the sum of {a} and {b} is {obj.add()}")

import math
class Circle:
    def __init__(self,radius):
        self.radius = radius

class cylinder(Circle):
    def __init__(self,radius,height):
        self.height = height
        super().__init__(radius)

    def volumemethod(self):
        return 4*math.pi*self.radius**2*self.height

a = eval(input("enter radius"))
b = eval(input("enter height"))

obj = cylinder(a, b)

print(f" the volume is %.2f" %obj.volumemethod())

# MULTIPLE INHERITANCE
class Big:
    def __init__(self, a):
        self.a = a

class Small:
    def __init__(self, b):
        self.b = b

class Middle(Big, Small):
    def __init__(self, a, b):
        Big().__init__(self, a)
        Small().__init__(self, b)
    def sum(self):
        return self.a + self.b

x,y = map(int, input("enter the number to be added").split())

obj = Middle(x, y)

print(f"the sum of the numbers is{obj.sum}")


#MULTI LEVEL INHERITANCE
import math

class Circle:
    def __init__(self,r):
    self.r = r
class Area(Circle):
    def area(self):
        return math.pi * self.r **2
class Display(Area):
    pass
rad = eval(input("enter value of the radius:"))

obj = Display(rad)

print(f"the area of the circle is {obj.area()}")


# HIERARCHICAL INHERITANCE
import math
class Circle:
    def __init__(self,r):
    self.r = r

class Area(Circle):
    def area(self):
        return math.pi * self.r ** 2

class Perimeter(Circle):
    def perimeter(self):
        return 2 * math.pi * self.r

rad = 7

obj1 = Area(rad)
obj2 = Perimeter(rad)

print(f"the area of the circle is {obj1.area()} while the perimeter is {obj2.perimeter()}")

"""
# HYBRID INHERITANCE
import math
class Circle:
    def __init__(self,r):
    self.r = r

class Area(Circle):
    def area(self):
        return math.pi * self.r ** 2

class Perimeter(Circle):
    def perimeter(self):
        return 2 * math.pi * self.r
class Display(Area,Perimeter):
    def display(self):
 print(f"the area of the circle is {self.area()} while the perimeter is {self.perimeter()}")
rad = 7

obj = Display(rad)
obj.display()




