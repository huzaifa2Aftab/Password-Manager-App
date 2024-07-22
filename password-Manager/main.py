from tkinter import *
from tkinter import messagebox
import json


def search_click():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            website = web_input.get()
    except FileNotFoundError:
        messagebox.showinfo("Error", "File not found.")
    else:
        if website in data:
            messagebox.showinfo(title="Info", message=f"Email:{data[website]["email"]}\n Password:{data[website]["password"]}")
        else:
            messagebox.showinfo(title="Error", message=f"Email:{website} not found.")



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen_click():
    import random

    number = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    special_letters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
    alpha_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                     "u", "v", "w", "x", "y", "z"]
    letters = random.randint(3, 4)
    symbols = random.randint(2, 4)
    numbers = random.randint(2, 4)
    password_1 = random.sample(alpha_letters, letters)
    password_2 = random.sample(number, numbers)
    password_3 = random.sample(special_letters, symbols)
    password = password_1 + password_2 + password_3
    random.shuffle(password)
    pas = ''.join(password)

    pass_input.delete(0, END)
    pass_input.insert(0, pas)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_click():
    web_data = web_input.get()
    user_data = user_input.get()
    pass_data = pass_input.get()
    new_data = {
        web_data: {
            "email": user_data,
            "password": pass_data
        }
    }

    if len(web_data) == 0 or len(pass_data) == 0:
        messagebox.showinfo("Error", "Please fill all the fields")
    else:
        is_ok = messagebox.askokcancel(title=web_data, message="Is it ok to save your data?")

    if is_ok:
        try:
            with open("data.json", 'r') as file:
                data = json.load(file)
        except :
            with open("data.json", 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", 'w') as file:
                json.dump(data, file, indent=4)
        finally:
            web_input.delete(0, END)
            pass_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.geometry('500x400')
window.title('Password Manager')
window.config(padx=30, pady=50)
lock_logo = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_logo)
canvas.grid(column=1, row=0)
web_label = Label(text='Website:', font=('Helvetica', 10))
web_label.grid(column=0, row=1)

web_input = Entry(width=34)
web_input.focus()
web_input.grid(column=1, row=1)
search_button = Button(text='Search', width=12, command=search_click)
search_button.grid(column=2, row=1)
user_label = Label(text='Email/Username:', font=('Helvetica', 10))
user_label.grid(column=0, row=2)
user_input = Entry(width=50)
user_input.insert(END, "huzaifaaftab614@gmail.com")
user_input.grid(column=1, row=2, columnspan=2)
pass_label = Label(text='Password:', font=('Helvetica', 10))
pass_label.grid(column=0, row=3)
pass_input = Entry(width=34)
pass_input.grid(column=1, row=3)
gen_button = Button(text='Gene-Password', width=12, command=gen_click)
gen_button.grid(column=2, row=3)
add_button = Button(text='Add ', width=43, command=add_click)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
