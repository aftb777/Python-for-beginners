# button = you click it, then it does stuff

from tkinter import *

count = 0
def click():
    global count
    count += 1
    print(f"{count}. You clicked the button")
    
window = Tk()

photo = PhotoImage(file='person.jpg')

window.title("Aftaab's Cohort")

button = Button(window ,
                text="click me!",
                command=click,
                font=("Comic Sans",30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound='top')
button.pack()

window.mainloop()