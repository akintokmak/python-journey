from tkinter import *
from tkinter import messagebox
from random import choice,shuffle,randint
import pyperclip
import json #New


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

# ------------------------------- SEARCH ----------------------------------- #

def find_password():
    try:
        with open("data.json","r") as data_file:
            data = json.load(data_file)
            website = website_entry.get()
            if len(website) > 0:
                messagebox.showinfo(title=website,message=f"Email: {data[website]["email"]}\n"
                                                          f"Password: {data[website]["password"]}")
            else:
                messagebox.showinfo(title="It cannot be empty!",message="Enter the word you want to search for.")
                website_entry.focus()
    except FileNotFoundError:
        messagebox.showinfo(title= "Oops",message="No Data File Found.")
    except KeyError:
        messagebox.showinfo(title="Not found",message=f"No details for the website: '{website}'")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    #Entries control
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
    }}

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
                                                           f"\n\nEmail :{email}"
                                                           f"\nPassword :{password}"
                                                           f"\n\nIs it ok to save?")
        if is_ok:
            # File Append
            try:
                with open("data.json", "r") as data_file:  # You don't have to close it.
                    # json.dump(new_data,data_file,indent=4) | json.dump -> Write
                    #Reading old data
                    data = json.load(data_file) #| json.load ->  Read
            except FileNotFoundError:
                with open("data.json","a") as data_file:
                    json.dump(new_data,data_file,indent = 4)
            else:
                #Updating old data with new data
                data.update(new_data)
                # Saving updated data
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                # Clear Entries
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()

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
website_entry = Entry(width=33)
website_entry.grid(column=1,row=1)
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

search_btn = Button(text= "Search",width=21,command=find_password)
search_btn.grid(column=2,row=1)




window.mainloop()