import tkinter as tk
from tkinter import messagebox


def login():
    username = entry_user.get()
    password = entry_pass.get()
    # In a real application you'd validate credentials here
    messagebox.showinfo("Login", f"Username: {username}\nPassword: {password}")


root = tk.Tk()
root.title("Login")
root.geometry("300x150")
root.resizable(False, False)

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(expand=True)

label_user = tk.Label(frame, text="Username:")
label_user.grid(row=0, column=0, sticky="e")

entry_user = tk.Entry(frame)
entry_user.grid(row=0, column=1, pady=5)

label_pass = tk.Label(frame, text="Password:")
label_pass.grid(row=1, column=0, sticky="e")

entry_pass = tk.Entry(frame, show="*")
entry_pass.grid(row=1, column=1, pady=5)

btn_login = tk.Button(frame, text="Login", command=login)
btn_login.grid(row=2, columnspan=2, pady=10)

root.mainloop()
