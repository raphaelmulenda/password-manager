"""Created By Raphael Mulenda (RFM) , start date Sun 24-April-2021"""
# import
import json
from random import choice, shuffle

from tkinter import *
from tkinter import messagebox

import pyperclip

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#008891"
Light_Green = "#3edbf0"
YELLOW = "#f7f5dd"
FONT_NAME = "Segoe UI"

# ---------------------------- UI SETUP ------------------------------- #
app = Tk()
app.title("Password Manager")
app.config(padx=30, pady=30, bg=GREEN)

canvas = Canvas(width=200, height=200, bg=GREEN, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img, anchor=CENTER)
canvas.grid(column=0, row=0)
data_frame = Frame(app, bd=10, bg=GREEN, width=500, height=200, relief=RIDGE)
data_frame.grid(column=0, row=1)
Sig_label = Label(app, text='RFM APP', font=(FONT_NAME, 10, 'bold'), bg=GREEN).grid(column=0, row=2)

# ---------------------------- Label creation------------------------------- #

website_label = Label(data_frame, text="Website:", bd=7, font=(FONT_NAME, 12, 'bold'), bg=GREEN)
website_label.grid(column=0, row=0)
user_name_label = Label(data_frame, text="Email/Username:", bd=7, font=(FONT_NAME, 12, 'bold'), bg=GREEN)
user_name_label.grid(column=0, row=1)
password_length = Label(data_frame, text="Password Length:", font=(FONT_NAME, 12, 'bold'), bg=GREEN)
password_length.grid(column=0, row=2)
password_label = Label(data_frame, text="Password:", bd=7, font=(FONT_NAME, 12, 'bold'), bg=GREEN)
password_label.grid(column=0, row=3)
# ---------------------------- VARIABLE------------------------------- #
WebSite = StringVar()
UserName = StringVar()
Password = StringVar()
Pass_len = IntVar()
# ---------------------------- Entry fields Creation------------------------------- #
website_entry = Entry(data_frame, font=(FONT_NAME, 12, 'bold'), textvariable=WebSite, bd=7, width=22)
website_entry.grid(column=1, row=0, padx=10, pady=10)
user_name_entry = Entry(data_frame, font=(FONT_NAME, 12, 'bold'), textvariable=UserName, bd=7, width=22)
user_name_entry.grid(column=1, row=1, padx=10, pady=5)
password_length_spinbox = Spinbox(data_frame, from_=8, to=32, font=(FONT_NAME, 12, 'bold'),
                                  textvariable=Pass_len, bd=5, width=21, relief=GROOVE, justify=CENTER)
password_length_spinbox.grid(column=1, row=2, padx=10, pady=10)
password_entry = Entry(data_frame, font=(FONT_NAME, 12, 'bold'), textvariable=Password, bd=7, width=22)
password_entry.grid(column=1, row=3, padx=10, pady=10)


# ---------------------------- FUNCTION------------------------------ #
def save_data():
    # This function will save the data to a json file that is sued a database and if the file doesnt exist
    # it will create a new one
    if WebSite.get() != "" and UserName.get() != "" and Password.get() != "":
        new_data = {
            WebSite.get(): {
                "username": UserName.get(),
                "password": Password.get()
            }
        }
        try:
            with open("database.json", "r") as db_json:
                # Reading Jason file (old data) if it exist
                data = json.load(db_json)
        except FileNotFoundError:
            # in case the file doesnt exit this code will create a new file and update it with new data
            with open("database.json", "w") as db_json:
                json.dump(new_data, db_json, indent=4, sort_keys=True)
        else:
            # if the file exist then this code will run and it will update the old the data with the new one
            data.update(new_data)
            # now the bellow code will save the updated data to our password database
            with open("database.json", "w") as db_json:
                json.dump(data, db_json, indent=4, sort_keys=True)
        finally:
            # this part will always run if the first statement is true
            WebSite.set("")
            UserName.set("")
            Password.set("")
            messagebox.showinfo(title='Data Saved', message="Data saved successfully")

        # this part will run if any of the fields is empty
    elif WebSite.get() == "" or UserName.get() == "" or Password.get() == "":
        messagebox.showwarning(title='Empty Fields', message="Don't leave any fields blank")


def search_data():
    if WebSite.get() != "":
        # the bellow code will search (iter) the entered website in the database and it will provide a feedback to user
        try:
            with open("database.json", "r") as db_json:
                # Reading Jason file (old data) if it exist
                data = json.load(db_json)
        except FileNotFoundError:
            # in case the file doesnt exist there will be a pop up message with an alert
            messagebox.showinfo(title="Not Data Found", message="No details for the website exists")
        except KeyError:
            messagebox.showinfo(title="Not Data Found", message="No details for the website exists")
        else:
            if f"{WebSite.get()}" in data:
                messagebox.showinfo(title=f"{WebSite.get()}",
                                    message=f"Email/Username: {data[f'{WebSite.get()}']['username']}\nPassword: "
                                            f"{data[f'{WebSite.get()}']['password']}")
                WebSite.set("")
            elif f"{WebSite.get()}" not in data:
                messagebox.showinfo(title="Not Data Found", message="No details for the website exists")
    elif WebSite.get() == "":
        messagebox.showwarning(title='Empty Fields', message="Enter a website!")


def copy_pass():
    # This function will copy the password to clipboard
    if Password.get() != "":
        pyperclip.copy(f"{Password.get()}")
        Password.set("")
        messagebox.showinfo(title="Copy to clipboard", message="Password copied to clipboard successfully")
    elif Password.get() == "":
        messagebox.showinfo(title="Empty Fields", message="The Password fields is empty, generate or enter a "

                                                          "password before copy to clipboard")


def generator():
    # This function will generate a random password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@']
    if Pass_len.get() <= 14:
        lst_letter = [choice(letters) for _ in range(Pass_len.get() - 4)]

        lst_symbol = [choice(symbols) for _ in range(2)]

        lst_number = [choice(numbers) for _ in range(2)]

        password_list = lst_letter + lst_symbol + lst_number
        shuffle(password_list)
        password = "".join(password_list)
        password_entry.delete(0, 'end')
        password_entry.insert(0, password)
        password_entry.config(fg='black')
        pyperclip.copy(password)
    elif Pass_len.get() > 14:
        lst_letter = [choice(letters) for _ in range(Pass_len.get() - 7)]

        lst_symbol = [choice(symbols) for _ in range(3)]

        lst_number = [choice(numbers) for _ in range(4)]

        password_list = lst_letter + lst_symbol + lst_number
        shuffle(password_list)
        password = "".join(password_list)
        password_entry.delete(0, 'end')
        password_entry.insert(0, password)
        password_entry.config(fg='black')
        pyperclip.copy(password)


# ---------------------------- Button Creation------------------------------- #

search_btn = Button(data_frame, bd=5, font=(FONT_NAME, 10, 'bold'), text="Search", width=14, bg=Light_Green,
                    command=search_data)
search_btn.grid(column=2, row=0, padx=10)
save_btn = Button(data_frame, bd=5, font=(FONT_NAME, 10, 'bold'), text="Save Data", width=14, bg=Light_Green,
                  command=save_data)
save_btn.grid(column=2, row=1, padx=5)
generate_btn = Button(data_frame, bd=5, font=(FONT_NAME, 10, 'bold'), text="Generate Password", width=14,
                      bg=Light_Green, command=generator)
generate_btn.grid(column=2, row=2, padx=5)
copy_pass_btn = Button(data_frame, bd=5, font=(FONT_NAME, 10, 'bold'), text="Copy Password", width=14, bg=Light_Green,
                       command=copy_pass)
copy_pass_btn.grid(column=2, row=3, padx=5)

app.resizable(FALSE, FALSE)
app.mainloop()
