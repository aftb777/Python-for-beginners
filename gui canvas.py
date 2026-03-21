# Canvas = widget that is used to draw graphs, plots, images in a window

from tkinter import *

window = Tk()

canvas = Canvas(window,height=500,width=500)
# canvas.create_line(0,0,500,500,fill="blue",width=5)
# canvas.create_line(0,500,500,0,fill="blue",width=5)

# canvas.create_rectangle(50,50,250,250,fill="purple")

# canvas.create_polygon(250,0,500,500,0,500,fill="yellow",outline="black",width=5)

# canvas.create_arc(0,0,500,500,style=ARC)# to flip this arc use start= (degrees) we want imside parenthesis

canvas.create_arc(0,0,500,500,fill='red',extent=180,width=10,outline='black')
canvas.create_arc(0,0,500,500,fill='white',extent=180,start=180,width=10,outline='black')
canvas.create_oval(190,190,310,310,fill='white',outline='black',width=10)
canvas.pack()

window.mainloop()