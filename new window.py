# from tkinter import *
# def create_window():
#     new_window = Tk() #Toplevel() = new window 'on top' of other windows linked to 'bottom' window
#                       #Tk() = new independant window
                     
#     old_window.destroy() # close out of old window
    
# old_window = Tk()

# Button(old_window,text="create new window",command=create_window).pack()

# old_window.mainloop()


# Create seperate tabs in our windows

from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window) #widget that manages a collection of windows 

tab1 = Frame(notebook)# new frame for tab1
tab2 = Frame(notebook)# new frame for tab2

notebook.add(tab1,text="tab 1")
notebook.add(tab2,text="tab 2")

notebook.pack(expand=True,fill="both")#expand = expand to fill any space not otherwise used 
                                      # fill = fill space on x and y axis

Label(tab1,text="hello,this is table 1",width=50,height=25).pack()
Label(tab2,text="goodbye,this is table 2",width=50,height=25).pack()

window.mainloop()