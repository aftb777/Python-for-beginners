# radio buttons = similar to checkbox, but you can only select one from a group

from tkinter import *

food = ["pizza" , "hamburger" , "hotdog"]

window = Tk()

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index], # adds text to radio buttons
                              variable=x, # groups radio button if they share the same var
                              value=index, # assigns each radio button a different value
                              padx=25,
                              pady=10,
                              font=("Imapct", 50)
                              )
    radiobutton.pack(anchor=W)
    
window.mainloop()