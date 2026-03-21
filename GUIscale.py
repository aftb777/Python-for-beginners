from tkinter import *

def submit():
    print("The temperature is: " + str(scale.get())+ " degrees celcius")

window = Tk()

scale = Scale(window, from_ = 100 , to = 0 ,
              length= 600,
              orient= VERTICAL , # orientation of scale
              font= ('Console',20),
              tickinterval=10, # adds a numeric indicators for value
            #   showvalue=0 # this will hide the current value
              resolution= 5 , # resolution of slider
              troughcolor= '#69EAFF', # gives icy blue color on slider
              fg= '#FF1C00',
              bg= 'black',
              )

# scale.set(50) put our scale on 50

scale.pack()

button = Button(window,text='submit',command=submit)
button.pack()

window.mainloop()