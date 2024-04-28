from tkinter import *

window = Tk()
window.title(" BEng20 ETE Students")
window.geometry("500x300")
Label(window, text="1.Dan Thon", font=("Aerial", 10)).grid(row=0, column=0,sticky=W)
Label(window, text="2.Beatrice Stephen", font=("Aerial", 10)).grid(row=1,column=0,sticky=W)
Label(window, text="3.John Haule", font=("Aerial", 10)).grid(row=2,column=0,sticky=W)
window.mainloop()



from tkinter import*
window = Tk()
window.title(" WELCOME DIT:")
window.geometry("500x300")
Label(window, text="Enter name", font=("Aerial", 10)).grid(row=0, column=0)
Label(window, text="Enter age", font=("Aerial", 10)).grid(row=1, column=0)
Entry(window, font=("Aerial", 10), width=10, borderwidth=5).grid(row=0, column=1)
Entry(window, font=("Aerial", 10), width=10, borderwidth=5).grid(row=1, column=1)
window.mainloop()



from tkinter import *

root = Tk()
root.geometry("500x300")
Label(root, text="Enter Full name").grid(row=0, column=0, sticky=W)
name = StringVar()
Entry(root, textvariable=name, width=25, borderwidth=10).grid(row=0, column=1)
Label(root, text="Registration number:").grid(row=1, column=0)
regNo = IntVar()
Entry(root, textvariable=regNo, width=25, borderwidth=10).grid(row=1, column=1)
Label(root, text="Course program").grid(row=2, column=0, sticky=W)
CourseProgram = StringVar()
Entry(root, textvariable=CourseProgram, width=25, borderwidth=10).grid(row=2, column=1)


def onclick():
    print(f"am {name.get()}, my regno is {regNo.get()}' i do {CourseProgram.get()}")


Button(root, text="CLICK", padx=10, pady=5, command=onclick).grid(row=3, column=2)

root.mainloop()



from tkinter import*

sum = Tk()
sum.title(" ADD NUMBERS:")
sum.geometry("250x50")
Label(sum, text="Enter the first number").place(x=200,y=50)
num1 = IntVar()
Entry(sum, textvariable=num1, width=10, borderwidth=6).place(x=350,y=50)
Label(sum, text=" Enter the second number", ).place(x=200,y=100)
num2 = IntVar()
Entry(sum, textvariable=num2, width=10, borderwidth=6).place(x=350,y=100)


def onclick():
    print(f" The sum of two numbers is {num1.get() + num2.get()}")


Button(sum, text="CLICK", fg="white", bg="black", padx=10, pady=3, command=onclick).place(x=320,y=150)
sum.mainloop()


from tkinter import *

window = Tk()
window.title(" MY NAME")
window.geometry("350x100")
Label(window,text= " Enter ur name").place(x=250,y=100)
Entry(window,width=10, borderwidth=5).place(x=350,y=100)
Button(window,text="Print my name",padx=10,pady=6).place(x=300,y=150)

window.mainloop()





#******************PACTICAL 8********************8

from tkinter import*

sum = Tk()
sum.title(" ADD NUMBERS:")
sum.geometry("250x50")
Label(sum, text="Enter the first number").place(x=200,y=50)
num1 = IntVar()
Entry(sum, textvariable=num1, width=10, borderwidth=6).place(x=350,y=50)
Label(sum, text=" Enter the second number" ).place(x=200,y=100)
num2 = IntVar()
Entry(sum, textvariable=num2, width=10, borderwidth=6).place(x=350,y=100)
obj= Label(sum,text=" ")
obj.place(x=320,y=200)

def onclick():
    Z = num2.get() + num1.get()
    obj.config(text="the sum is " + str(Z))

Button(sum, text="CLICK", fg="white", bg="black", padx=10, pady=3, command=onclick).place(x=320,y=150)
sum.mainloop()




from tkinter import*

sum = Tk()
sum.title(" AREA OF RECTANGLE:")
sum.geometry("250x50")
Label(sum, text="Enter Length").place(x=200,y=50)
Length = IntVar()
Entry(sum, textvariable=Length, width=10, borderwidth=6).place(x=350,y=50)
Label(sum, text=" Enter WIDTH", ).place(x=200,y=100)
width = IntVar()
Entry(sum, textvariable=width, width=10, borderwidth=6).place(x=350,y=100)


def onclick():
    print(f" The sum of two numbers is {Length.get() * width.get()}")


Button(sum, text="CLICK", fg="white", bg="black", padx=10, pady=3, command=onclick).place(x=320,y=150)
sum.mainloop()



from tkinter import *
root = Tk()#1. Create window or frame
#2. Think about the Structure and put components into the window
number = IntVar()
e=Entry(textvariable=number,font=12,fg="white",bg="black",width=30,borderwidth=20)
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
    print("The average is ",sum/5)

Button(text="7", font=12,fg="white",bg="black",padx=30,command=lambda : onclickF(7)).grid(row=1,column=0)
Button(text="5", font=12,fg="white",bg="black",padx=30,command=lambda : onclickF(5)).grid(row=1,column=1)
Button(text="4", font=12,fg="white",bg="black",padx=30,command=lambda : onclickF(4)).grid(row=1,column=2)
Button(text="3", font=12,fg="white",bg="black",padx=30,command=lambda : onclickF(3)).grid(row=2,column=0)
Button(text="Clr", font=12,fg="white",bg="black",padx=24,command=clear).grid(row=3,column=0)
Button(text="0", font=12,fg="white",bg="black",padx=30,command=lambda : onclickF(0)).grid(row=2,column=1)
Button(text="+", font=12,fg="white",bg="black",padx=30,command=add).grid(row=3,column=1)
Button(text="1", font=12,fg="white",bg="black",padx=30,command=lambda : onclickF(1)).grid(row=2,column=2)
Button(text="=", font=12,fg="white",bg="black",padx=30,command=equal).grid(row=3,column=2)
root.mainloop()




from tkinter import *
root = Tk()#1. Create window or frame
#2. Think about the Structure and put components into the window
number = IntVar()
e=Entry(textvariable=number,font=12,fg="white",bg="black",width=30,borderwidth=20)
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
    print("The average is ",sum/5)

Button(text="7", font=12,fg="white",bg="black",padx=30,command=lambda : onclickF(7)).grid(row=1,column=0)
Button(text="5", font=12,fg="white",bg="black",padx=30,command=lambda : onclickF(5)).grid(row=1,column=1)
Button(text="4", font=12,fg="white",bg="black",padx=30,command=lambda : onclickF(4)).grid(row=1,column=2)
Button(text="3", font=12,fg="white",bg="black",padx=30,command=lambda : onclickF(3)).grid(row=2,column=0)
Button(text="Clr", font=12,fg="white",bg="black",padx=24,command=clear).grid(row=3,column=0)
Button(text="0", font=12,fg="white",bg="black",padx=30,command=lambda : onclickF(0)).grid(row=2,column=1)
Button(text="+", font=12,fg="white",bg="black",padx=30,command=add).grid(row=3,column=1)
Button(text="1", font=12,fg="white",bg="black",padx=30,command=lambda : onclickF(1)).grid(row=2,column=2)
Button(text="=", font=12,fg="white",bg="black",padx=30,command=equal).grid(row=3,column=2)
root.mainloop()
"""



from tkinter import *
root = Tk()#1. Create window or frame
#2. Think about the Structure and put components into the window
number = IntVar()
e=Entry(textvariable=number,font=12,fg="white",bg="black",width=30,borderwidth=20)
e.grid(row=0,column=0,columnspan=3)
#step 3 create event methods and any other method
def onclickF(number):
    s = e.get()
    e.delete(0, END)
    e.insert(0, s + str(number))
def clear():
    e.delete(0,END)
def mult():
    fnum = e.get()
    global num
    num = int(fnum)
    e.delete(0,END)
def equal():
    snum = e.get()
    e.delete(0,END)
    e.insert(0,num*int(snum))
Button(text="0", font=12,fg="white",bg="black",padx=30,command=lambda : onclickF(0)).grid(row=1,column=0)
Button(text="1", font=12,fg="white",bg="black",padx=30,command=lambda : onclickF(1)).grid(row=1,column=1)
Button(text="2", font=12,fg="white",bg="black",padx=30,command=lambda : onclickF(2)).grid(row=1,column=2)
Button(text="-5", font=12,fg="white",bg="black",padx=28,command=lambda : onclickF(-5)).grid(row=2,column=0)
Button(text="Clr", font=12,fg="white",bg="black",padx=25,command=clear).grid(row=3,column=1)
Button(text="9", font=12,fg="white",bg="black",padx=30,command=lambda : onclickF(9)).grid(row=2,column=1)
Button(text="x", font=12,fg="white",bg="black",padx=30,command=mult).grid(row=2,column=2)
Button(text="=", font=12,fg="white",bg="black",padx=30,command=equal).grid(row=3,column=2)
root.mainloop()

