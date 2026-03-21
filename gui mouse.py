from tkinter import *

def dosomething(event):
    print("Mouse Co-ordinates " + str(event.x) + "," + str(event.y)) # gives coordinates where we have clicked
    
window = Tk()

window.bind("<Button-1>",dosomething) # press left mouse button to do something button-2 for scroll wheel
# button-3 for right mouse button
# ButtonRelease (if we are pressing our button and scrolling and then realease it will print coordinates till where we have dragged)
# Enter as same as Button-1
# Motion where the mouse moved
window.mainloop()