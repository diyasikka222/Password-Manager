import tkinter as tk
from tkinter import messagebox
import pyperclip
import password_logic as pl

def add_password():
    name = entry_account.get()  # Gets the account name entered by the user
    pwd = entry_password.get()  # Gets the password entered by the user

    if not name or not pwd:
        messagebox.showwarning("Input Error", "Please fill in both fields.")
        return

    pl.add_password(name, pwd)  # Calls the function from the password_logic module to save the password
    entry_account.delete(0, tk.END)  # Clears the text box after saving
    entry_password.delete(0, tk.END)  # Clears the password field
    messagebox.showinfo("Success", f"Password for '{name}' added!")

def view_passwords():
    passwords = pl.get_all_passwords()  # Retrieves the saved passwords

    if not passwords:
        messagebox.showinfo("Saved Passwords", "No passwords found.")
        return

    new_window = tk.Toplevel(root)  # Creates a new top-level window to display saved passwords
    new_window.title("Saved Passwords")
    new_window.geometry("400x300")

    for acc, pw in passwords:
        frame = tk.Frame(new_window)
        frame.pack(pady=5, anchor="w", padx=10)

        tk.Label(frame, text=f"Account: {acc}", font=("Arial", 10, "bold")).pack(anchor="w")
        tk.Label(frame, text=f"Password: {pw}", font=("Arial", 10)).pack(anchor="w")

        copy_btn = tk.Button(frame, text="Copy Password", command=lambda p=pw: pyperclip.copy(p))
        copy_btn.pack(anchor="w", pady=2)

# --- Start the Tkinter GUI ---
root = tk.Tk()  # Create the main window
root.title("Password Manager")
root.geometry("400x250")
root.resizable(False, False)

tk.Label(root, text="Account Name:").pack(pady=5)
entry_account = tk.Entry(root, width=40)  # Text box for account name
entry_account.pack()

tk.Label(root, text="Password:").pack(pady=5)
entry_password = tk.Entry(root, width=40, show="*")  # Text box for password
entry_password.pack()

tk.Button(root, text="Add Password", command=add_password).pack(pady=10)
tk.Button(root, text="View Passwords", command=view_passwords).pack()

root.mainloop()  # Start the Tkinter event loop
