from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

FILE_PATH = "./src/030B - passmanager/"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def generate_password():
    letters = []
    for x in range(97, 123):
        letters.append(chr(x))

    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def open_json(mode="r"):
    data_file = open(FILE_PATH + "data.json", mode)
    return data_file


def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        blank_fields_msgbx()
    else:
        try:
            # try to open the file
            with open_json("r") as data_file:
                data = json.load(data_file)

            # if the json exits but is empty
        except json.decoder.JSONDecodeError as j:
            with open_json("w") as data_file:
                json.dump(new_data, data_file, indent=4)

            # if the file doesn't exist, create it
        except FileNotFoundError as e:
            with open_json("w") as data_file:
                json.dump(new_data, data_file, indent=4)

            # if the data variable is not referenced
        except UnboundLocalError as u:
            print(f"{u} has not been initialized")

        else:
            # if the file exists then update it
            data.update(new_data)
            with open_json("w") as data_file:
                json.dump(data, data_file, indent=4)

        # clear data entry form after update
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            if not data_file.closed:
                data_file.close()
        # end try


def blank_fields_msgbx(
    title="Oops", msg="Please make sure you haven't left any fields empty."
):
    messagebox.showinfo(
        title=title,
        message=msg,
    )


def find_password():
    if len(website_entry.get()) == 0:
        blank_fields_msgbx()
    else:
        with open_json("r") as data_file:
            # with open(FILE_PATH + "data.json", "r") as data_file:
            data = json.load(data_file)
            key_list = list(data.keys())
            key = website_entry.get()
            if key in key_list:
                user = data[key]["email"]
                pw = data[key]["password"]
                show_msg(user, pw)
            else:
                blank_fields_msgbx(
                    "No Match",
                    "Sorry the website name you entered could not be found.",
                )


def copy_pw(text):
    pyperclip.copy(text)


def show_msg(user, pw):
    from tkinter import ttk

    root = Tk()
    root.title("Press the button to copy the password")
    root.resizable(False, False)
    root.geometry("400x100")

    options = {"fill": "both", "padx": 10, "pady": 10, "ipadx": 5}

    ttk.Label(
        root, text=f"Username: {user}\nPassword: {pw}"
    ).pack(**options)
    ttk.Button(
        root, text="Copy", command=copy_pw(pw)
    ).pack(side=RIGHT, padx=15)
    root.mainloop()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="./src/030B - passmanager/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="e")
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="e")
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="e")

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")
email_entry.insert(0, "bryan@gmail.com")
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, sticky="w")

# Buttons
generate_password_button = Button(
    text="Generate Password", command=generate_password, width=15
)
generate_password_button.grid(row=3, column=2, sticky="e")
add_button = Button(text="Add", width=29, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2, sticky="e")

window.mainloop()
