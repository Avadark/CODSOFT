import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_label.config(text=password)

def reset_password():
    password_label.config(text="")
    length_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Password Generator")

# Styling
root.configure(bg="#F5F5F5")
root.geometry("300x250")
root.resizable(False, False)

title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"), bg="#F5F5F5")
title_label.pack(pady=(20, 10))

length_label = tk.Label(root, text="Password Length:", bg="#F5F5F5")
length_label.pack()

length_entry = tk.Entry(root, font=("Helvetica", 12))
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", font=("Helvetica", 12), command=generate_password)
generate_button.pack(pady=(10, 10))

password_label = tk.Label(root, text="", font=("Courier", 12, "bold"), bg="#F5F5F5", wraplength=280)
password_label.pack()

reset_button = tk.Button(root, text="Reset", font=("Helvetica", 12), command=reset_password)
reset_button.pack(pady=(10, 20))

root.mainloop()
