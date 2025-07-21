import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox


def fade_in(window, interval=20, step=0.05, alpha=0.0):
    """Gradually fade in the window for a smooth appearance."""
    if alpha < 1.0:
        window.attributes("-alpha", alpha)
        window.after(interval, fade_in, window, interval, step, alpha + step)
    else:
        window.attributes("-alpha", 1.0)


app = ttk.Window(themename="cyborg")
app.title("Hackboot Login")
app.geometry("500x300")
app.resizable(False, False)
app.attributes("-alpha", 0.0)


# Create main frame
container = ttk.Frame(app, padding=20)
container.pack(expand=True, fill=BOTH)

# Animated title
title = ttk.Label(container, text="Hackboot", font=("Helvetica", 28, "bold"), bootstyle=INFO)

def slide_title(y=-50):
    if y < 20:
        title.place(relx=0.5, y=y, anchor="n")
        app.after(10, slide_title, y + 5)
    else:
        title.place(relx=0.5, y=20, anchor="n")

title.place(relx=0.5, y=-50, anchor="n")

# Login form
form = ttk.Frame(container)
form.place(relx=0.5, rely=0.45, anchor="center")

lbl_user = ttk.Label(form, text="Username:")
lbl_user.grid(row=0, column=0, sticky=E, pady=5, padx=5)
entry_user = ttk.Entry(form, width=30)
entry_user.grid(row=0, column=1, pady=5)

lbl_pass = ttk.Label(form, text="Password:")
lbl_pass.grid(row=1, column=0, sticky=E, pady=5, padx=5)
entry_pass = ttk.Entry(form, show="*", width=30)
entry_pass.grid(row=1, column=1, pady=5)


def login():
    username = entry_user.get()
    password = entry_pass.get()
    Messagebox.ok(f"Username: {username}\nPassword: {password}", title="Login")


btn = ttk.Button(form, text="Login", bootstyle=SUCCESS, command=login)
btn.grid(row=2, columnspan=2, pady=(15, 0))

app.after(0, fade_in, app)
app.after(200, slide_title)
app.mainloop()
