from tkinter import *
from tkinter import messagebox

def click():
    # messagebox.showinfo(title='This is aninfo message box',message='You are a person')
    # messagebox.showwarning(title='WARNING',message='You have a virus')
    # messagebox.showerror(title='ERROR',message='Something went wrong')
    # if messagebox.askokcancel(title='ask ok cancel',message='Do you want to the thing'):
    #     print("You did a thing")
    # else:
    #     print("You cancelled a thing")
    
    # if messagebox.askretrycancel(title='ask ok cancel',message='Do you want to retry the thing'):
    #     print("You retried a thing")
    # else:
    #     print("You cancelled a thing")
    
    # if messagebox.askyesno(title='ask yes or no',message='do you like cake'):
    #     print("I like cake too")
    # else:
    #     print("Why do you not like cake")
    
    # answer = messagebox.askquestion(title='ask question',message='Do you like pie?')
    # if(answer == 'yes'):
    #     print("i like pie too")
    # else:
    #     print("Why you dont like pie")
    
    answer = messagebox.askyesnocancel(title= 'yes no cancel',message='Do you like to code?',icon='warning')
    if (answer == True):
            print("Nice")
    elif(answer == False):
        print("Then why you are watching this video about coding")
    else:
        print("You have dogged the question")        
        
window = Tk()

button = Button(window,command=click,text='click me')
button.pack()

window.mainloop()