import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox


def fade_in(window, interval=20, step=0.05, alpha=0.0):
    """Gradually fade in the window for a smooth appearance."""
    if alpha < 1.0:
        window.attributes('-alpha', alpha)
        window.after(interval, fade_in, window, interval, step, alpha + step)
    else:
        window.attributes('-alpha', 1.0)


def login():
    username = entry_user.get()
    password = entry_pass.get()
    Messagebox.ok(f"Username: {username}\nPassword: {password}", title="Login")


app = ttk.Window(themename="superhero")
app.title("Login")
app.geometry("340x200")
app.resizable(False, False)
app.attributes('-alpha', 0.0)

frame = ttk.Frame(app, padding=20)
frame.pack(expand=True, fill=BOTH)

label_user = ttk.Label(frame, text="Username:")
label_user.grid(row=0, column=0, sticky=E, pady=5)
entry_user = ttk.Entry(frame, width=25)
entry_user.grid(row=0, column=1, pady=5)

label_pass = ttk.Label(frame, text="Password:")
label_pass.grid(row=1, column=0, sticky=E, pady=5)
entry_pass = ttk.Entry(frame, show="*", width=25)
entry_pass.grid(row=1, column=1, pady=5)

btn_login = ttk.Button(frame, text="Login", bootstyle=SUCCESS, command=login)
btn_login.grid(row=2, columnspan=2, pady=(15, 0))

app.after(0, fade_in, app)
app.mainloop()
