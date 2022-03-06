from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_letters + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website=website_entry.get()
    username=username_entry.get()
    password=password_entry.get()
    new_data= {website: {"email": username,
                         "password": password,
                         }
               }


    if website == "" or username =="" or password =="":
        messagebox.showerror(title="Empty Field", message="You left an empty field")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data,data_file, indent=4)

        else:
            data.update(new_data)
            with open("data.json","w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            username_entry.delete(0, END)
            password_entry.delete(0, END)


def search_acc():
    site_search = website_entry.get()
    try:
        with open("data.json", "r") as accounts:
            ind_account = json.load(accounts)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="This data file doesn't exist")
    else:
        if site_search in ind_account:
            site = ind_account[site_search]
            username = site["email"]
            password = site["password"]
            messagebox.showinfo(title = f"{site_search} Credentials", message = f"Your login is: {username}\nYour password is: {password}")
        else:
            messagebox.showinfo(title="Error", message="Account not found")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
locker_img=PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=locker_img)
canvas.grid(column=1, row=0)

website_text = Label(text="Website:")
website_text.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

username_text = Label(text="Email/Username:")
username_text.grid(column=0, row=2)

username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)

password_text = Label(text="Password:")
password_text.grid(column=0, row=3)

password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)

password_button = Button(text="Generate Password", command=generate_pass)
password_button.grid(column = 3, row=3)

add_button = Button(text="Add", width=35, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", command=search_acc)
search_button.grid(column = 3, row=1)

window.mainloop()