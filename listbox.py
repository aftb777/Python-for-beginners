# listbox = A listening of selectabale text items within its own container

def submit():
    food=[]
    
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
        
    print("You have ordered : ")
    for index in food:
        print(index)
    
def add():
    listbox.insert(listbox.size(),entrybox.get())
    listbox.config(height=listbox.size())
    
def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())
    
from tkinter import *

window = Tk()

listbox = Listbox(window,
                  bg="black",
                  font=("Constantia",35),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"burger")
listbox.insert(4,"soup")
listbox.insert(5,"salad")

listbox.config(height=listbox.size())#adjust the size of menu

entrybox = Entry(window)
entrybox.pack()

frame = Frame(window)
frame.pack()

submitbutton = Button(frame,text= "submit",command=submit)
submitbutton.pack()

addbox = Button(frame,text="add",command=add)
addbox.pack()

deletebutton = Button(frame,text="delete",command=delete)
deletebutton.pack(side= LEFT)

window.mainloop()