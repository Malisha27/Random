import customtkinter as ctk
import tkinter.messagebox as tkmb

# Selecting GUI theme - dark, light, system (for system default)
ctk.set_appearance_mode("dark")
# Selecting color theme - blue, green, dark-blue
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x400")
app.title("WinPro")


def login():
    username = "admin"
    password = "admin"
    new_window = ctk.CTkToplevel(app)

    new_window.title("Login Page")
    new_window.geometry("350x150")

    if user_entry.get() == username and user_pass.get() == password:
        tkmb.showinfo(
            # title="Login Successful",
            # message="You have logged in Successfully"
            # i want to open a new page called waterSystemanagement, its going to be  a separate file in the code
        )
        # ctk.CTkLabel(
        #     new_window,
        #     text="GeeksforGeeks is best for learning ANYTHING !!"
        # ).pack()
    elif user_entry.get() == username and user_pass.get() != password:
        tkmb.showwarning(
            title='Wrong password',
            message='Please check your password'
        )
    elif user_entry.get() != username and user_pass.get() == password:
        tkmb.showwarning(
            title='Wrong username',
            message='Please check your username'
        )
    else:
        tkmb.showerror(
            title="Login Failed",
            message="Invalid Username and password"
        )


frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=40, fill='both', expand=True)

# Title Label
title_label = ctk.CTkLabel(
    master=frame,
    text='Validate Credentials',
    font=("Arial", 16, "bold")
)
title_label.pack(pady=12, padx=10)

# Username Label and Entry
username_label = ctk.CTkLabel(master=frame, text="Username:")
username_label.pack(pady=2, padx=10)

user_entry = ctk.CTkEntry(master=frame, placeholder_text="Enter your username")
user_entry.pack(pady=12, padx=10)

# Password Label and Entry
password_label = ctk.CTkLabel(master=frame, text="Password:")
password_label.pack(pady=2, padx=10)

user_pass = ctk.CTkEntry(master=frame, placeholder_text="Enter your password", show="*")
user_pass.pack(pady=12, padx=10)

# Remember Me Checkbox
checkbox = ctk.CTkCheckBox(master=frame, text='Remember Me')
checkbox.pack(pady=12, padx=10)

# Login Button
button = ctk.CTkButton(master=frame, text='Login', command=login)
button.pack(pady=12, padx=10)

app.mainloop()
