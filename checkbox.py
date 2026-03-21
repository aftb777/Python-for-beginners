from tkinter import *

def display():
    if(x.get()):
        print("You agree")
    else:
        print("You dont agree :(")

window = Tk()

x = BooleanVar() # instead of this we can also use another data types too

photo = PhotoImage(file='person.jpg')

check_button = Checkbutton(window ,
                        text="I agree",
                        variable=x,
                        onvalue=True,
                        offvalue=False,
                        command=display,
                        font=('Arial' , 20),
                        fg='#00FF00',
                        bg='black',
                        activeforeground='#00FF00',
                        activebackground='black',
                        padx=25,
                        pady=10,
                        image=photo,
                        compound='left')

check_button.pack()

window.mainloop()