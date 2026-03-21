# grid() = geometry manager that organize widgets in table like structure in a parent

from tkinter import *

window =Tk()

title = Label(window,text="Enter your info",font=("Arial",25)).grid(row=0,column=0,columnspan=2)

firstNamelabel = Label(window,text='First name : ',width=20,bg="red").grid(row=1,column=0)
firstNameentry = Entry(window).grid(row=1,column=1)

lastNamelabel = Label(window,text='last name : ',width=20,bg="green").grid(row=2,column=0)
lastNameentry = Entry(window).grid(row=2,column=1)

emaillabel = Label(window,text='E-mail name : ',width=20,bg="yellow").grid(row=3,column=0)
emailentry = Entry(window).grid(row=3,column=1)

submit_button = Button(window,text="submit").grid(row=4,column=0,columnspan=2)

window.mainloop()