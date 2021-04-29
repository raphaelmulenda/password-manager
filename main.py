from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#008891"
YELLOW = "#f7f5dd"
FONT_NAME = "Segoe UI"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
app = Tk()
app.title("Password Manager")
app.config(padx=50, pady=50, bg=GREEN)

canvas = Canvas(width=200, height=200, bg=GREEN, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img, anchor=CENTER)
canvas.grid(column=0, row=0)
data_frame = Frame(app, bd=10, bg=GREEN, width=500, height=200, relief=RIDGE)
data_frame.grid(column=0, row=1)

# Label creation
website_label = Label(data_frame, text="Website:", bd=7, font=(FONT_NAME, 12, 'bold'), bg=GREEN)
website_label.grid(column=0, row=0)
user_name_label = Label(data_frame, text="Email/Username:", bd=7, font=(FONT_NAME, 12, 'bold'), bg=GREEN)
user_name_label.grid(column=0, row=1)
password_length = Label(data_frame, text="Password Length:", font=(FONT_NAME, 12, 'bold'), bg=GREEN)
password_length.grid(column=0, row=2)
password_label = Label(data_frame, text="Password:", bd=7, font=(FONT_NAME, 12, 'bold'), bg=GREEN)
password_label.grid(column=0, row=3)

# Entry fields Creation
website_entry = Entry(data_frame, font=(FONT_NAME, 12, 'bold'), textvariable='website', bd=7, width=32)
website_entry.grid(column=1, row=0, padx=10, pady=10)
user_name_entry = Entry(data_frame, font=(FONT_NAME, 12, 'bold'), textvariable='username', bd=7, width=32)
user_name_entry.grid(column=1, row=1, padx=10, pady=5)
password_length_spinbox = Spinbox(data_frame, from_=8, to=32, font=(FONT_NAME, 12, 'bold'),textvariable='password_length', bd=5, width=15, relief=GROOVE, justify=CENTER)
password_length_spinbox.grid(column=1, row=2, padx=10, pady=10)
password_entry = Entry(data_frame, font=(FONT_NAME, 12, 'bold'), textvariable='password', bd=7, width=32)
password_entry.grid(column=1, row=3, padx=10, pady=10)

# Button Creation

app.resizable(FALSE, FALSE)
app.mainloop()
