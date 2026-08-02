from tkinter import *
from tkinter import messagebox
from random import choice,shuffle,randint
import pyperclip



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    #Entries control
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website == "":
        messagebox.showinfo(title="Oops",message="Please fill website!")
        website_entry.focus()
    elif email == "":
        messagebox.showinfo(title="Oops", message="Please fill email!")
        email_entry.focus()
    elif password == "":
        messagebox.showinfo(title="Oops", message="Please fill password!")
        password_entry.focus()
    else:
        is_ok = messagebox.askyesno(title=website, message=f"These are the details entered:"
                                                           f"\nEmail :{email}"
                                                           f"\nPassword :{password}"
                                                           f"\nIs it ok to save?")
        if is_ok:
            # File Append
            try:
                with open("data.txt", "a") as data_file:  # You don't have to close it.
                    data_file.write(f"{website} | {email} | {password}\n")
                # Clear Entries
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()
            except Exception as e:
                print(e)
                messagebox.showwarning(title="Warning",message="Could not be saved, please try again.")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

#Logo
canvas = Canvas(width=200,height=200,highlightthickness=0)
logo_img = PhotoImage(file= "logo.png")
canvas.create_image(100,100 ,image = logo_img)
canvas.grid(column=1,row=0)

#Labels
website_label = Label(text = "Website :",justify="right")

website_label.grid(column=0,row=1)
email_label = Label(text = "Email/Password :")
email_label.grid(column=0,row=2)
password_label = Label(text = "Password :")
password_label.grid(column=0,row=3)

label = Label(text="",width=50)
label.grid(column=1,row=5,columnspan=2)

#Entries
website_entry = Entry(width=59)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()
email_entry = Entry(width=59)
email_entry.insert(0,"akinntok.45@gmail.com")
email_entry.grid(column=1,row=2,columnspan=2)

password_entry = Entry(width=33)
password_entry.grid(column=1,row=3)


#Buttons
generate_password_btn = Button(text = "Generate Password",width=21,command=generate_password)
generate_password_btn.grid(column=2,row=3)

add_btn = Button(text="Add",width=50,command=save)
add_btn.grid(column=1,row=4,columnspan=2)




window.mainloop()