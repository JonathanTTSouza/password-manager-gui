"""
Password manager. Generates passwords, and also stores it.
"""

from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    """Generates strong password"""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = ''.join(password_list)

    password_entry.delete(0, END)  # clears textbox so it doesn't append to previous generated password

    password_entry.insert(index=0, string=password)
    pyperclip.copy(password)  # copies password to clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Command for save button. Writes the website, email and password to data.txt if conditions are met"""
    # If any field is empty, show error
    if website_entry.get() == '' or email_entry.get() == '' or password_entry == '':
        messagebox.showerror('Error', 'Please fill the empty fields')
    else:
        # User confirmation
        if messagebox.askokcancel(title=website_entry.get(),
                                  message=f'Email: {email_entry.get()}\nPassword: {password_entry.get()}\nIs this '
                                          f'correct?'):
            # Writes info to data.txt
            with open('data.txt', 'a') as file:
                file.write(f'{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n')

            # Clears fields
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
# WINDOW
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# CANVAS/LOGO
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# LABELS
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# ENTRIES
website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky='EW')  # sticky='EW' = sticks content to 'EAST' and 'WEST' of column.
website_entry.focus()

email_entry = Entry()
email_entry.grid(column=1, row=2, columnspan=2, sticky='EW')
# email_entry.insert(END, email@email.com) -> used if you want pre formatted email

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky='EW')

# BUTTONS
generate_password_button = Button(text='Generate Password', command=password_generator)
generate_password_button.grid(column=2, row=3, sticky='EW')

add_button = Button(text='Add', command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky='EW')

# Keeps the program running (Necessary)
window.mainloop()
