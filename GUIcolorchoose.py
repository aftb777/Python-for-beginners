from tkinter import *
from tkinter import colorchooser

def click():
    color = colorchooser.askcolor()
    print(color)
    colorHex = color[1] # element at position 2
    print(colorHex)
    window.config(bg=colorHex) # change background color
    
    # window.config(bg=colorchooser.askcolor()[1]) # shortcut method

window = Tk()

window.geometry("420x420")
button = Button(text='click me',command=click)
button.pack()

window.mainloop()