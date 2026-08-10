BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random

current_card = {}
word_list = {}
word_to_know = []
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/english_words.csv")
    word_list = original_data.to_dict(orient="records")
else:
    word_list = data.to_dict(orient="records")

flip_timer = None

def next_card():
    global current_card, flip_timer
    if flip_timer is not None:
        window.after_cancel(flip_timer)
    current_card = random.choice(word_list)
    canvas.itemconfig(card_word,text = current_card["English"],fill="black")
    canvas.itemconfig(card_title,text="English",fill="black")
    canvas.itemconfig(canvas_image,image = card_front_img)
    flip_timer = window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(canvas_image,image = card_back_img)
    canvas.itemconfig(card_word,text=current_card["Turkish"],fill="white")
    canvas.itemconfig(card_title,text="Türkçe",fill="white")

#Buttons Scripts
def wrong_click():
    next_card()

def right_click():

    word_to_know.append(current_card)
    word_list.remove(current_card)
    data = pandas.DataFrame(word_list)
    data_known_word = pandas.DataFrame(word_to_know)
    data_known_word.to_csv("data/words_to_know.csv",index=False)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)


canvas = Canvas(width=800,height=526,)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400,263,image=card_front_img)

canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
card_title = canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text="Word",font=("Ariel",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)

#Buttons
cross_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=cross_img,highlightthickness=0,command=wrong_click)
wrong_btn.grid(column=0,row=1)

check_img = PhotoImage(file="images/right.png")
right_btn = Button(image=check_img,highlightthickness=0,command=right_click)
right_btn.grid(column=1,row=1)

next_card()





window.mainloop()