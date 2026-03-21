# frame = rectangular container to group and hold widgets

from tkinter import *

window = Tk()

frame = Frame(window,bg="blue",bd=5,relief=RAISED)
frame.place(x=0,y=0)

# best way or second way for buttons

Button(window,text="W",font=("Consolas",25),width=3).pack(side=TOP)
Button(window,text="A",font=("Consolas",25),width=3).pack(side=LEFT)
Button(window,text="S",font=("Consolas",25),width=3).pack(side=LEFT)
Button(window,text="D",font=("Consolas",25),width=3).pack(side=LEFT)

window.mainloop()