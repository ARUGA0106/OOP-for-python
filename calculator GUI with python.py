"""""
# practical 8 
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
"""""

"""""
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
"""""

# QN 3
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
"""""

"""""
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
"""""

#Qn 6.
"""""
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
"""""

#qn 7
"""""
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
"""""

#Qn 8.
"""""

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
"""""

"""""
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
"""""

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