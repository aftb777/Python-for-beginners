from tkinter import * 

def dosomething(event):
    # print(f"You pressed {event.keysym}") to print what you have pressed
    label.config(text=event.keysym) # it shows what are you typing on pycharm
    
window = Tk()

window.bind("<Key>",dosomething) # Syntax : bind(event,function)

label = Label(window,font=("Helvetica",100))
label.pack()

window.mainloop()