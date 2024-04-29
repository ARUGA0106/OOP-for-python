"""
last update: 22 march 2024
This script consists of sample codes for various python basics, with no error each code block perform its own principle remember to extract it and run in your IDEs. Install neccesary libraries to use advanced code systems you’ll need to write Python programs. Many of
these concepts are common to all programming languages, so they’ll be useful throughout your life as a programmer.
happy learning.

"""


#first program
print("Hello, World!")

# Variables
x = 5
y = "Hello"

# Data Types

# Integer
age = 25
# Float
height = 5.9
# String
name = "John"
# Boolean
is_student = True

# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements
print(my_list[0])  # Output: 1

# Modifying elements
my_list[0] = 10

# Adding elements
my_list.append(6)

# Removing elements
my_list.remove(3)

# Looping through a list
for item in my_list:
    print(item)
    
# Creating a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Accessing values
print(my_dict['name'])  # Output: John

# Modifying values
my_dict['age'] = 30

# Adding new key-value pairs
my_dict['gender'] = 'Male'

# Looping through a dictionary
for key, value in my_dict.items():
    print(key, value)
    
# Creating a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Accessing values
print(my_dict['name'])  # Output: John

# Modifying values
my_dict['age'] = 30

# Adding new key-value pairs
my_dict['gender'] = 'Male'

# Looping through a dictionary
for key, value in my_dict.items():
    print(key, value)
    
# Creating a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Accessing values
print(my_dict['name'])  # Output: John

# Modifying values
my_dict['age'] = 30

# Adding new key-value pairs
my_dict['gender'] = 'Male'

# Looping through a dictionary
for key, value in my_dict.items():
    print(key, value)
    
# Defining a function
def greet(name):
    return "Hello, " + name + "!"

# Calling a function
print(greet("Alice"))  # Output: Hello, Alice!
# Defining a function
def greet(name):
    return "Hello, " + name + "!"

# Calling a function
print(greet("Alice"))  # Output: Hello, Alice!

# Defining a class
class Car:
    def __init__(self, make, model
# Defining a class
class Car:
    def __init__(self, make, model
    
# Hello World
print("Hello, World!")

# Variables and Data Types
x = 5
y = "Hello"
age = 25
height = 5.9
name = "John"
is_student = True

# Lists
my_list = [1, 2, 3, 4, 5
]
print(my_list[0])  # Output: 1
my_list[0] = 10
my_list.append(6)
my_list.remove(3)
for item in my_list:
    print(item)
    

# Dictionaries
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict['name'])  # Output: John
my_dict['age'] = 30
my_dict['gender'] = 'Male'
for key, value in my_dict.items():
    print(key, value)


# Functions
def greet(name):
    return "Hello, " + name + "!"

print(greet("Alice"))  # Output: Hello, Alice!


# Classes and Objects (OOP)
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def info(self):
        return f"{self.year} {self.make} {self.model}"

my_car = Car("Toyota", "Camry", 2020)
print(my_car.info())  # Output: 2020 Toyota Camry

# Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.name, "says", dog.sound())  # Output: Buddy says Woof!
print(cat.name, "says", cat.sound())  # Output: Whiskers says Meow!


# Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            return amount
        else:
            return "Insufficient funds"

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
print(account.withdraw(2000))  # Output: Insufficient funds
print(account.get_balance())  # Output: 1500


# Polymorphism
def make_sound(animal):
    print(animal.sound())

make_sound(dog)  # Output: Woof!
make_sound(cat)  # Output: Meow!


# Basic Data Analysis Tasks
import numpy as np
import pandas as pd


# Creating a DataFrame
data = {'Name': ['John', 'Alice', 'Bob', 'Emily'],
        'Age': [25, 30, 35, 28],
        'Salary': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)


# Displaying the DataFrame
print(df)

# Calculating mean salary
mean_salary = np.mean(df['Salary'])
print("Mean Salary:", mean_salary)


# Filtering data
above_30 = df[df['Age'] > 30]
print("Above 30:\n", above_30)
import math


# Function to calculate the area of a rectangle
def rectangle_area(length, width):
    return length * width


# Function to calculate the area of a circle
def circle_area(radius):
    return math.pi * radius**2


# Function to calculate the area of a triangle
def triangle_area(base, height):
    return 0.5 * base * height


# Example usage
length = 5
width = 4
radius = 3
base = 6
height = 8

print("Area of rectangle:", rectangle_area(length, width))
print("Area of circle:", circle_area(radius))
print("Area of triangle:", triangle_area(base, height))
import random


# Function to estimate the value of π using the Monte Carlo method
def monte_carlo_pi(num_points):
    points_inside_circle = 0
    total_points = 0

    for _ in range(num_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2 + y**2
        if distance <= 1:
            points_inside_circle += 1
        total_points += 1

    return 4 * (points_inside_circle / total_points)


# Example usage
num_points = 1000000
estimated_pi = monte_carlo_pi(num_points)
print("Estimated value of π using Monte Carlo method:", estimated_pi)
import numpy as np


# Function to calculate the area of a rectangle
def rectangle_area(length, width):
    return length * width

# Function to calculate the area of a circle
def circle_area(radius):
   
   return np.pi * radius**2

# Function to calculate the area of a triangle
def triangle_area(base, height):
    return 0.5 * base * height


# Example area calculation
length = 5
width = 4
radius = 3
base = 6
height = 8

print("Area of rectangle:", rectangle_area(length, width))
print("Area of circle:", circle_area(radius))
print("Area of triangle:", triangle_area(base, height))

#if statements
x = 5
if x > 0:
    print("x is positive")
    
#if-else statements
x = -3
if x > 0:
    print("x is positive")
else:
    print("x is non-positive")
    
    
#iff statements
x = 0
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")
    
    
#nested if
x = 10
if x > 0:
    if x % 2 == 0:
        print("x is positive and even")
    else:
        print("x is positive and odd")
        
        
#while loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1
    
    
#while loop with else
count = 0
while count < 5:
    print("Count:", count)
    count += 1
else:
    print("Loop finished")
    
    
#for loop
for i in range(5):
    print("Value:", i)
    
    
#for loop over list
my_list = [1, 2, 3, 4, 5]
for num in my_list:
    print("Number:", num)
    
    
#for loop with else
for i in range(5):
    print("Value:", i)
else:
    print("Loop finished")
    
    
#looping with the string
word = "Python"
for char in word:
    print("Character:", char)
    
    
#looping with the dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
    
    
#looping with tuple
my_tuple = ((1, 2), (3, 4), (5, 6))
for t in my_tuple:
    print("Tuple:", t)
    
    
#looping with pass
for i in range(5):
    pass  # Placeholder for future code
    
#looping with the zip
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print("Name:", name, "Age:", age)
    
#looping with backward
my_list = [1, 2, 3, 4, 5]
for i in reversed(my_list):
    print("Value:", i)
    
#FUTHER EXAMPLES 

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

#working with python GUI


# QN 1.
from tkinter import*
window = Tk()   # create window { open
window.title("Add Number")
window.geometry("250x50")
Label(window, text=" Enter First Number: ", font=(" Ariel",12)).place(x =5, y = 10) # full name position
obj = Label(window, text="", font=(" Ariel",12))
obj.place(x =200, y = 100)
num1 = IntVar()
Entry(window,textvariable = num1, font=(" Ariel",12),width=25,borderwidth=10).place(x = 200, y = 10)
Label(window, text=" Enter the second number: ", font=(" Ariel",12)).place(x =5, y = 50)
num2 = IntVar()
Entry(window,textvariable = num2, font=(" Ariel",12),width=25,borderwidth=10).place(x = 200, y = 50)
def onlick():
    sum = num1.get() + num2.get()
    obj.config( text = f" the sum of {num1.get()} and {num2.get()}is  { sum}")
Button(window, text=" print sum ", font=(" Ariel",12),fg="red",padx=10,pady=3,command=onlick).place(x =200, y = 130)
window.mainloop()


# QN 2
from tkinter import*
window = Tk()
window.title("Area of rectangle")
window.geometry("500x300")
Label(window, text="Enter width of rectangle: ", font=(" Ariel",10)).place(x =5, y = 10) # full name position
width = IntVar()
Entry(window,textvariable = width, font=(" Ariel",10),width=25,borderwidth=10).place(x = 200, y = 10)
Label(window, text="Enter length of rectangle: ", font=(" Ariel",10)).place(x =5, y = 50)
length = IntVar()
Entry(window,textvariable = length, font=(" Ariel",10),width=25,borderwidth=10).place(x = 200, y = 50)
def onlick():
    area = width.get() * length.get()
    print(f" the sum is  { area}")
Button(window, text=" print area ", font=(" Ariel",10),fg="red",padx=10,pady=3,command=onlick).place(x =200, y = 130)
window.mainloop()


# QN 3

from tkinter import *
window = Tk()
window.title(" display of number")
window.geometry("500x300")
def onclick(number):
  obj.insert(0,number)
data = IntVar()
obj = Entry(window,textvariable=data,font=("Ariel",10,"bold"),width=20,bd=50,fg="black",bg="white",justify="right")
obj.grid(row=0,columnspan=3)
Button(window, text=" 7 ", font=(" Ariel",10,"bold"),fg="black",padx=10,pady=3,command=lambda :onclick(7)).grid(row=1,column=0)
Button(window, text=" 8 ", font=(" Ariel",10,"bold"),fg="black",padx=10,pady=3,command=lambda :onclick(8)).grid(row=1,column=1)
Button(window, text=" 9 ", font=(" Ariel",10,"bold"),fg="black",padx=10,pady=3,command=lambda :onclick(9)).grid(row=1,column=2)
Button(window, text=" 6 ", font=(" Ariel",10,"bold"),fg="black",padx=10,pady=3,command=lambda :onclick(6)).grid(row=2,column=0)
Button(window, text=" 5 ", font=(" Ariel",10,"bold"),fg="black",padx=10,pady=3,command=lambda :onclick(5)).grid(row=2,column=1)
Button(window, text=" 4 ", font=(" Ariel",10,"bold"),fg="black",padx=10,pady=3,command=lambda :onclick(4)).grid(row=2,column=2)
Button(window, text=" 3 ", font=(" Ariel",10,"bold"),fg="black",padx=10,pady=3,command=lambda :onclick(3)).grid(row=3,column=0)
Button(window, text=" 2 ", font=(" Ariel",10,"bold"),fg="black",padx=10,pady=3,command=lambda :onclick(2)).grid(row=3,column=1)
Button(window, text=" 1 ", font=(" Ariel",10,"bold"),fg="black",padx=10,pady=3,command=lambda :onclick(1)).grid(row=3,column=2)
window.mainloop()


#GN 4
from tkinter import*
window = Tk()
window.title("simple calculator")
#window.geometry("300x200")
def onclick(number):
  e.insert(0,number)
data = IntVar()
e = Entry(window,textvariable=data,font=("Ariel",10,"bold"),width=20,bd=50,fg="black",bg="green",justify="right")
e.grid(row=0,columnspan=3)
Button(window, text=" 7 ", font=(" Ariel",10,"bold"),fg="blue",borderwidth=5,padx=10,pady=3,command=lambda :onclick(7)).grid(row=1,column=0)
Button(window, text=" 8 ", font=(" Ariel",10,"bold"),fg="blue",borderwidth=5,padx=10,pady=3,command=lambda :onclick(8)).grid(row=1,column=1)
Button(window, text=" 9 ", font=(" Ariel",10,"bold"),fg="blue",borderwidth=5,padx=10,pady=3,command=lambda :onclick(9)).grid(row=1,column=2)
Button(window, text=" 6 ", font=(" Ariel",10,"bold"),fg="blue",borderwidth=5,padx=10,pady=3,command=lambda :onclick(6)).grid(row=2,column=0)
Button(window, text=" 5 ", font=(" Ariel",10,"bold"),fg="blue",borderwidth=5,padx=10,pady=3,command=lambda :onclick(5)).grid(row=2,column=1)
Button(window, text=" 4 ", font=(" Ariel",10,"bold"),fg="blue",borderwidth=5,padx=10,pady=3,command=lambda :onclick(4)).grid(row=2,column=2)
Button(window, text=" 3 ", font=(" Ariel",10,"bold"),fg="blue",borderwidth=5,padx=10,pady=3,command=lambda :onclick(3)).grid(row=3,column=0)
Button(window, text=" 2 ", font=(" Ariel",10,"bold"),fg="blue",borderwidth=5,padx=10,pady=3,command=lambda :onclick(2)).grid(row=3,column=1)
Button(window, text=" 1 ", font=(" Ariel",10,"bold"),fg="blue",borderwidth=5,padx=10,pady=3,command=lambda :onclick(1)).grid(row=3,column=2)
Button(window, text=" 0 ", font=(" Ariel",10,"bold"),fg="blue",borderwidth=5,padx=10,pady=3,command=lambda :onclick(0)).grid(row=4,column=0)
Button(window, text=" Clear ", font=(" Ariel",10,"bold"),fg="blue",borderwidth=5,padx=40,pady=3,command=onclick).grid(row=4,column=1,columnspan=2)
Button(window, text=" + ", font=(" Ariel",10,"bold"),fg="blue",borderwidth=5,padx=10,pady=3,command=onclick).grid(row=5,column=0)
Button(window, text=" = ", font=(" Ariel",10,"bold"),fg="blue",borderwidth=5,padx=10,pady=3,command=onclick).grid(row=5,column=1)

window.mainloop()
"""""
#QN No 5
"""""
from tkinter import *
window = Tk()
window.title(" display of number")
window.geometry("500x300")
def onclick(number):
  obj.insert(0,number)
data = IntVar()
obj = Entry(window,textvariable=data,font=("Ariel",10,"bold"),width=20,bd=50,fg="black",bg="white",justify="right")
obj.grid(row=0,columnspan=3)
Button(window, text=" 1 ", font=(" Ariel",10,"bold"),fg="black",padx=10,pady=3,command=lambda :onclick(7)).grid(row=1,column=0)
Button(window, text=" 2 ", font=(" Ariel",10,"bold"),fg="black",padx=10,pady=3,command=lambda :onclick(8)).grid(row=1,column=1)
Button(window, text=" 3 ", font=(" Ariel",10,"bold"),fg="black",padx=10,pady=3,command=lambda :onclick(9)).grid(row=1,column=2)
Button(window, text=" 4 ", font=(" Ariel",10,"bold"),fg="black",padx=10,pady=3,command=lambda :onclick(6)).grid(row=2,column=0)
Button(window, text=" 5 ", font=(" Ariel",10,"bold"),fg="black",padx=10,pady=3,command=lambda :onclick(5)).grid(row=2,column=1)
Button(window, text=" 6 ", font=(" Ariel",10,"bold"),fg="black",padx=10,pady=3,command=lambda :onclick(4)).grid(row=2,column=2)
Button(window, text=" 7 ", font=(" Ariel",10,"bold"),fg="black",padx=10,pady=3,command=lambda :onclick(3)).grid(row=3,column=0)
Button(window, text=" 8 ", font=(" Ariel",10,"bold"),fg="black",padx=10,pady=3,command=lambda :onclick(2)).grid(row=3,column=1)
Button(window, text=" 9 ", font=(" Ariel",10,"bold"),fg="black",padx=10,pady=3,command=lambda :onclick(1)).grid(row=3,column=2)
Button(window, text=" 0 ", font=(" Ariel",10,"bold"),fg="black",padx=10,pady=3,command=lambda :onclick(1)).grid(row=4,column=0)
window.mainloop()

#Qn 6.

from tkinter import *
window = Tk()#1. Create window or frame
#2. Think about the Structure and put components into the window
number = IntVar()
e=Entry(textvariable=number,font=12,fg="white",bg="green",width=30,borderwidth=20)
e.grid(row=0,column=0,columnspan=3)
#step 3 create event methods and any other method
def onclickF(number):
    s = e.get()
    e.delete(0, END)
    e.insert(0, s + str(number))
def clear():
    e.delete(0,END)
def division():
    fnum = e.get()
    global num
    num = float(fnum)
    e.delete(0,END)
def equal():
    snum = e.get()
    e.delete(0,END)
    e.insert(0,num / int(snum))

Button(text="7", font=12,fg="black",padx=30,command=lambda : onclickF(7)).grid(row=1,column=0)
Button(text="5", font=12,fg="black",padx=30,command=lambda : onclickF(5)).grid(row=1,column=1)
Button(text="4", font=12,fg="black",padx=30,command=lambda : onclickF(4)).grid(row=1,column=2)
Button(text="3", font=12,fg="black",padx=30,command=lambda : onclickF(3)).grid(row=2,column=0)
Button(text="Clr", font=12,fg="black",padx=24,command=clear).grid(row=3,column=0)
Button(text="0", font=12,fg="black",padx=30,command=lambda : onclickF(0)).grid(row=2,column=1)
Button(text="/", font=12,fg="black",padx=30,command=division).grid(row=3,column=1)
Button(text="1", font=12,fg="black",padx=30,command=lambda : onclickF(1)).grid(row=2,column=2)
Button(text="=", font=12,fg="black",padx=30,command=equal).grid(row=3,column=2)
window.mainloop()


#qn 7

from tkinter import *
root = Tk()#1. Create window or frame
#2. Think about the Structure and put components into the window
number = IntVar()
e=Entry(textvariable=number,font=12,fg="white",bg="green",width=30,borderwidth=20)
e.grid(row=0,column=0,columnspan=3)
#step 3 create event methods and any other method
def onclickF(number):
    s = e.get()
    e.delete(0, END)
    e.insert(0, s + str(number))
def clear():
    e.delete(0,END)
def add():
    fnum = e.get()
    global num
    num = int(fnum)
    e.delete(0,END)
def equal():
    snum = e.get()
    e.delete(0,END)
    e.insert(0,num + int(snum))
    sum = num + int(snum)
    print(f" the sum is {sum}")

Button(text="7", font=12,fg="black",padx=30,command=lambda : onclickF(7)).grid(row=1,column=0)
Button(text="5", font=12,fg="black",padx=30,command=lambda : onclickF(5)).grid(row=1,column=1)
Button(text="4", font=12,fg="black",padx=30,command=lambda : onclickF(4)).grid(row=1,column=2)
Button(text="3", font=12,fg="black",padx=30,command=lambda : onclickF(3)).grid(row=2,column=0)
Button(text="Clr", font=12,fg="black",padx=24,command=clear).grid(row=3,column=0)
Button(text="0", font=12,fg="black",padx=30,command=lambda : onclickF(0)).grid(row=2,column=1)
Button(text="+", font=12,fg="black",padx=30,command=add).grid(row=3,column=1)
Button(text="1", font=12,fg="black",padx=30,command=lambda : onclickF(1)).grid(row=2,column=2)
Button(text="=", font=12,fg="black",padx=30,command=equal).grid(row=3,column=2)
root.mainloop()




from tkinter import *
root = Tk()#1. Create window or frame
#2. Think about the Structure and put components into the window
number = IntVar()
e=Entry(textvariable=number,font=12,fg="white",bg="green",width=30,borderwidth=20)
e.grid(row=0,column=0,columnspan=3)
#step 3 create event methods and any other method
def onclickF(number):
    s = e.get()
    e.delete(0, END)
    e.insert(0, s + str(number))
def clear():
    e.delete(0,END)
def add():
    fnum = e.get()
    global num
    num = float(fnum)
    e.delete(0,END)
def equal():
    snum = e.get()
    e.delete(0,END)
    e.insert(0,num + float(snum))
    global sum
    sum = num + float(snum)
    avarage = sum/5
    print(f" the avarage is {avarage}")

Button(text="1", font=12,fg="black",padx=30,command=lambda : onclickF(1)).grid(row=1,column=0)
Button(text="2", font=12,fg="black",padx=30,command=lambda : onclickF(2)).grid(row=1,column=1)
Button(text="3", font=12,fg="black",padx=30,command=lambda : onclickF(3)).grid(row=1,column=2)
Button(text="4", font=12,fg="black",padx=30,command=lambda : onclickF(4)).grid(row=2,column=0)
Button(text="5", font=12,fg="black",padx=30,command=lambda : onclickF(5)).grid(row=2,column=1)
Button(text="6", font=12,fg="black",padx=30,command=lambda : onclickF(4)).grid(row=2,column=2)
Button(text="Clr", font=12,fg="black",padx=24,command=clear).grid(row=4,column=0)
Button(text="0", font=12,fg="black",padx=30,command=lambda : onclickF(0)).grid(row=3,column=1)
Button(text="+", font=12,fg="black",padx=30,command=add).grid(row=4,column=1)
Button(text="1", font=12,fg="black",padx=30,command=lambda : onclickF(1)).grid(row=3,column=2)
Button(text="=", font=12,fg="black",padx=30,command=equal).grid(row=4,column=2)
root.mainloop()



# QN NO 9
from tkinter import *
root = Tk()#1. Create window or frame
#2. Think about the Structure and put components into the window
number = IntVar()
e=Entry(textvariable=number,font=12,fg="white",bg="green",width=30,borderwidth=20)
e.grid(row=0,column=0,columnspan=3)
#step 3 create event methods and any other method
def onclickF(number):
    s = e.get()
    e.delete(0, END)
    e.insert(0, s + str(number))
def clear():
    e.delete(0,END)
def add():
    fnum = e.get()
    global num
    num = float(fnum)
    e.delete(0,END)
def equal():
    snum = e.get()
    e.delete(0,END)
    e.insert(0,num + float(snum))
    sum = num + float(snum)
    print(" the sum of entered number is", sum)

Button(text="1", font=12,fg="black",padx=30,command=lambda : onclickF(1)).grid(row=1,column=0)
Button(text="2", font=12,fg="black",padx=30,command=lambda : onclickF(2)).grid(row=1,column=1)
Button(text="3", font=12,fg="black",padx=30,command=lambda : onclickF(3)).grid(row=1,column=2)
Button(text="4", font=12,fg="black",padx=30,command=lambda : onclickF(4)).grid(row=2,column=0)
Button(text="5", font=12,fg="black",padx=30,command=lambda : onclickF(5)).grid(row=2,column=1)
Button(text="6", font=12,fg="black",padx=30,command=lambda : onclickF(4)).grid(row=2,column=2)
Button(text="Clr", font=12,fg="black",padx=24,command=clear).grid(row=4,column=0)
Button(text="0", font=12,fg="black",padx=30,command=lambda : onclickF(0)).grid(row=3,column=1)
Button(text="+", font=12,fg="black",padx=30,command=add).grid(row=4,column=1)
Button(text="1", font=12,fg="black",padx=30,command=lambda : onclickF(1)).grid(row=3,column=2)
Button(text="=", font=12,fg="black",padx=30,command=equal).grid(row=4,column=2)
root.mainloop()


from tkinter import *
root = Tk()#1. Create window or frame
#2. Think about the Structure and put components into the window
number = IntVar()
e=Entry(textvariable=number,font=12,fg="white",bg="green",width=30,borderwidth=20)
e.grid(row=0,column=0,columnspan=3)
#step 3 create event methods and any other method
def onclickF(number):
    s = e.get()
    e.delete(0, END)
    e.insert(0, s + str(number))
def clear():
    e.delete(0,END)
def add():
    fnum = e.get()
    global num
    num = float(fnum)
    e.delete(0,END)
def equal():
    snum = e.get()
    e.delete(0,END)
    e.insert(0,num + float(snum))
    global sum
    sum = num + float(snum)
    avarage = sum/5
    print("The avarage is of entered number %.3f is " %avarage)

Button(text="1", font=12,fg="black",padx=30,command=lambda : onclickF(1)).grid(row=1,column=0)
Button(text="2", font=12,fg="black",padx=30,command=lambda : onclickF(2)).grid(row=1,column=1)
Button(text="3", font=12,fg="black",padx=30,command=lambda : onclickF(3)).grid(row=1,column=2)
Button(text="4", font=12,fg="black",padx=30,command=lambda : onclickF(4)).grid(row=2,column=0)
Button(text="5", font=12,fg="black",padx=30,command=lambda : onclickF(5)).grid(row=2,column=1)
Button(text="6", font=12,fg="black",padx=30,command=lambda : onclickF(4)).grid(row=2,column=2)
Button(text="7", font=12,fg="black",padx=30,command=lambda : onclickF(4)).grid(row=3,column=0)
Button(text="8", font=12,fg="black",padx=30,command=lambda : onclickF(5)).grid(row=3,column=1)
Button(text="9", font=12,fg="black",padx=30,command=lambda : onclickF(4)).grid(row=3,column=2)
Button(text="0", font=12,fg="black",padx=30,command=lambda : onclickF(0)).grid(row=4,column=0)
Button(text="Clr", font=12,fg="black",padx=24,command=clear).grid(row=5,column=0)
Button(text="+", font=12,fg="black",padx=30,command=add).grid(row=5,column=1)
Button(text="=", font=12,fg="black",padx=30,command=equal).grid(row=5,column=2)
root.mainloop()


#UP NEXT PYTHON FOR DATA ANALYST





