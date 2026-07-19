from tkinter import *


#pack , place , grid
#You can't use two method in together pack and grid. Just choose one or another.
window = Tk()
window.title("TKINTER")
window.minsize(width=500,height=500)

#Label

my_label = Label(text="I'm a Label.",font=("Arial",24,"bold"))
# my_label.pack() #side="left"
# my_label.place(x=0,y=0)
my_label.grid(column=0,row=0)


#Button
def button_clicked():
    # my_label["text"] = "I got clicked" You can use one of them.
    # my_label.config(text="I got clicked")
    my_label.config(text=input.get())
button = Button(text = "Click Me",command=button_clicked)
# button.pack()
button.grid(column=1,row=1)
#New Button
def button_two_clicked():
    my_label.config(text="Button 2 Clicked.")

button2 = Button(text ="Click Me 2",command=button_two_clicked)
button2.grid(column=2,row=0)
#Entry (Input)
input = Entry(width=15)
# input.pack()
input.grid(column=3,row=2)



window.mainloop()
