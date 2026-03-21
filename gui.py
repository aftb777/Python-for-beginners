from tkinter import *

# widgets = GUI elements : buttons , textboxes , labels , images
# windows = serves as a container to hold or contain these widgets

window = Tk() # instantiate an instance of a window

window.title("Aftaab's GUI Program") #title of GUI

window.geometry("420x420") # set the size 420x420 is height and width

# icon = PhotoImage(file= '') to set icon for GUI type link inside the ''
# window.iconphoto(True , icon)

window.config(background= "red") # for background colors 
# TIP : type "hex value color" on google for ur fav colors and type hex value using #

window.mainloop() # place window on computer screen, listen for events