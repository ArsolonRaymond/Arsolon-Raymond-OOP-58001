from tkinter import *
from tkinter import ttk
window = Tk()
window.geometry("500x250+10+20")
window.title("Midterm in OOP")

def Ditonamepo():
    txtfld['text'] = 'tistent'

label = Label(window, text = "Enter your fullname:", fg = "red")
label.place(x=60, y=70)

button = Button(window, text = "Click to display your Fullname", fg = "red", command=Ditonamepo)
button.place (x=60, y=145)

txtfld = Entry(window, text = 'tistent', bd = 5)
txtfld.place(x=265, y=65)

txtfld = Entry(window, text = 'testingname' , bd = 5)
txtfld.place(x=265, y=145)

window.mainloop()