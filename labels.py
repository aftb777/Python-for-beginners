# label = an area widget that holds text and/or an image within a window

from tkinter import *

window = Tk()

photo = PhotoImage(file='person.jpg')
label = Label(window ,
              text= "Hello ",
              font= ('Arial',40,'bold'),
              fg='white',
              bg='black',
              relief=RAISED,# relief for borders
              bd=10,
              padx=20,
              pady=20,
              image=photo)

label.pack()  #one way to add label
# label.place(x=0 , y=0) # second way to print label

window.mainloop()