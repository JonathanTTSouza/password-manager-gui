"""
Password manager. Generates passwords, and also stores it.
"""
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


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
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    # If any field is empty, show error
    if website == '' or email == '' or password == '':
        messagebox.showerror('Error', 'Please fill the empty fields')
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            # Clears fields
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- SEARCH FUNCTION ---------------------------#
def find_password():
    website = website_entry.get()
    password = password_entry.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
            messagebox.showinfo(f'Website: {data[website]}\nPassword: {password}')
    except KeyError:
        messagebox.showerror('Error', 'No details for the website exists')
    except FileNotFoundError:
        messagebox.showerror('Error', 'No Data File Found')
    except:
        messagebox.showerror('Error', 'Unknown Error')


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
website_entry.grid(column=1, row=1, sticky='EW')  # sticky='EW' = sticks content to 'EAST' and 'WEST' of column.
website_entry.focus()

email_entry = Entry()
email_entry.grid(column=1, row=2, columnspan=2, sticky='EW')
# email_entry.insert(END, email@email.com) -> used if you want pre formatted email

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky='EW')

# BUTTONS
search_button = Button(text='Search', command=find_password)
search_button.grid(column=2, row=1, sticky='EW')

generate_password_button = Button(text='Generate Password', command=password_generator)
generate_password_button.grid(column=2, row=3, sticky='EW')

add_button = Button(text='Add', command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky='EW')

# Keeps the program running (Necessary)
window.mainloop()
