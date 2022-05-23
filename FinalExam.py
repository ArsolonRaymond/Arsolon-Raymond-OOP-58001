from tkinter import *

window = Tk()
window.title("Find the largest number")
window.geometry("500x180+20+10")

def findSmallest(): #defin
    Real = []
    Real.append(eval(conOfent2.get()))
    Real.append(eval(conOfent3.get()))
    Real.append(eval(conOfent4.get()))
    smallestNumber.set(min(Real))

label1 = Label(window, text = "The Program that Finds the Least Number")
label1.grid(row=0, column=1, columnspan=1,sticky=EW)
label2 = Label(window,text = "Enter the first number:")
label2.grid(row=1, column = 0,sticky=W)

conOfent2 = StringVar()

entry2 = Entry(window,bd=3,textvariable=conOfent2)
entry2.grid(row=1, column = 1)

label3 = Label(window,text = "Enter the second number:")
label3.grid(row=2, column=0)

conOfent3=StringVar()

entry3 = Entry(window,bd=3,textvariable=conOfent3)
entry3.grid(row=2,column=1)

label4 = Label(window,text="Enter the third number:")
label4.grid(row=3,column =0, sticky=W)

conOfent4 = StringVar()

entry4 = Entry(window,bd=3,textvariable=conOfent4)
entry4.grid(row=3, column=1)

buttn1 = Button(window,text = "Find Smallest Number",command=findSmallest)
buttn1.grid(row=4, column = 1)

label5 = Label(window,text="The largest number:")
label5.grid(row=5,column=0,sticky=W)

smallestNumber = StringVar()

entry5 = Entry(window,bd=3,state="readonly",textvariable=smallestNumber)
entry5.grid(row=5,column=1)


mainloop()