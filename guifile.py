from tkinter import *

from tkinter import filedialog

def openfile():
    filepath = filedialog.askopenfilename(initialdir="//Users//aftaabmulla//Documents//Screenshot 2023-12-21 at 7.40.27 PM.jpg",
                                          title="Open file okay?")
    # print(filepath) use this to open and copy path of file
    file = open(filepath,'r')
    print(file.read())
    file.close()
    
    
window = Tk()

button = Button(text="Open",command=openfile)
button.pack()

window.mainloop()

# GUI save file(filedailog)

# from tkinter import *
# from tkinter import filedialog

# def savefile():
#     file = filedialog.asksaveasfile()
#     filetext = str(text.get(1.0,END))
#     file.write(filetext)
#     file.close
    
# window = Tk()

# button = Button(text='save',command=savefile)
# button.pack()

# text = Text(window)
# text.pack()

# window.mainloop()