from tkinter import *


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20,pady=20)

def miles_to_km():
    miles = float(mile_input.get())
    km = miles * 1.609
    return km

def button_clicked():
    kilo_result_label.config(text=str(miles_to_km()))

#From label
from_label = Label(text = "From:")
from_label.grid(column=0,row=0)
#To label
to_label = Label(text = "To:")
to_label.grid(column=0,row=1)
#Mile Entry
mile_input = Entry(width=20)
mile_input.grid(column=1,row=0)
mile_input.bind("<Return>",lambda event: button_clicked())
#Mile Label
mile_label = Label(text = "Mile")
mile_label.grid(column=2,row=0)
#Kilometer Result Label
kilo_result_label = Label(text="0")
kilo_result_label.grid(column=1,row=1)
#Kilometer Label
kilo_label = Label(text="Kilometer")
kilo_label.grid(column=2,row=1)
#Convert Button
convert_button = Button(text = "Convert",width=15,command=button_clicked)
convert_button.grid(column=1,row=2)




window.mainloop()