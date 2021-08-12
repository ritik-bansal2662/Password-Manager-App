from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

#----------------------------- FIND PASSWORD ------------------------------------------#

def find_password():
    web = input_website.get()
    if len(web)==0:
        messagebox.showinfo(title="Oops", message="please make sure you haven't left the website field empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No data file found.")
        else:
            if web in data:
                email_msg = data[web]["email"]
                pass_web = data[web]["password"]
                messagebox.showinfo(title=web, message=f"Email: {email_msg}\nPassword: {pass_web}")
            else:
                messagebox.showinfo(title="Oops", message=f"No password saved for {web}.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

def generate_random_pass():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_sym = [choice(symbols) for _ in range(randint(2, 4))]
    password_num = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_num + password_sym + password_letters

    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    input_pass.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = input_website.get()
    email = input_email.get()
    password = input_pass.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="please make sure you haven't left any field empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                #reading the old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #updating old data with new data
            data.update(new_data)
            #writing data to the file
            with open("data.json", "w") as new_file:
                json.dump(data, new_file, indent=4)
        finally:
            input_website.delete(0, END)
            input_pass.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
#window.minsize(width=400, height=400)
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(height=200, width=200)
pass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_image)
canvas.grid(column=1, row=0)


website_label = Label(text="Website:")
website_label.grid(column=0, row=1)


email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)


pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)


input_website = Entry(width=17)
input_website.grid(column=1, row=1)
input_website.focus()


input_email = Entry(width=35)
input_email.grid(column=1, row=2, columnspan=2)
input_email.insert(END, "ritikbansal539@gmail.com")

input_pass = Entry(width=17)
input_pass.grid(column=1, row=3)


gen_pass_button = Button(text="Generate Password", width=14, command=generate_random_pass)
gen_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=29, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1)



window.mainloop()
