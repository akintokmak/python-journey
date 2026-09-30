import requests
from tkinter import *

def get_quote():
    response = requests.get(url="https://ataturk.now.sh/tr")
    response.raise_for_status()

    data = response.json()
    quote_new_text = data["quote"] + "\n\nMustafa Kemal Atatürk."
    canvas.itemconfig(quote_text,text=quote_new_text)

window = Tk()
window.title("Mustafa Kemal Atatürk Sözleri")
window.config(padx=50,pady=50)

canvas = Canvas(width=703,height=400)
background_img = PhotoImage(file="boardnew.png")
canvas.create_image(351,200,image=background_img)
quote_text = canvas.create_text(500,200,width=250,font=("Arial",11,"bold"),fill="white")
canvas.grid(row=0,column=0,)

canvas_img = Canvas(width=10,height=600)
ataturk_img = PhotoImage(file="Ataturk.png")
canvas.create_image(225,300,image = ataturk_img)
canvas_img.grid(row=0,column=1)

next_quote_btn = Button(text="Sözler İçin Tıkla",width=50,highlightthickness=0,command=get_quote)
next_quote_btn.grid(row=1,column=0)




window.mainloop()