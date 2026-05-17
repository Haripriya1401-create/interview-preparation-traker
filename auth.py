import customtkinter as ctk
from tkinter import messagebox
from database import Database

class AuthPage:
    def __init__(self, root):
        self.root = root
        self.db = Database()
        self.root.title("Interview Preparation Tracker")
        self.root.geometry("500x500")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.create_login_ui()

    # ---------------- LOGIN UI ---------------- #
    def create_login_ui(self):
        self.clear_window()
        title = ctk.CTkLabel(
            self.root,
            text="Interview Tracker Login",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=30)
        self.username_entry = ctk.CTkEntry(
            self.root,
            placeholder_text="Username",
            width=250
        )
        self.username_entry.pack(pady=10)
        self.password_entry = ctk.CTkEntry(
            self.root,
            placeholder_text="Password",
            show="*",
            width=250
        )
        self.password_entry.pack(pady=10)
        login_button = ctk.CTkButton(
            self.root,
            text="Login",
            command=self.login
        )
        login_button.pack(pady=20)
        register_button = ctk.CTkButton(
            self.root,
            text="Register",
            command=self.create_register_ui
        )
        register_button.pack(pady=10)

    # ---------------- REGISTER UI ---------------- #
    def create_register_ui(self):
        self.clear_window()
        title = ctk.CTkLabel(
            self.root,
            text="Create Account",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=30)
        self.new_username = ctk.CTkEntry(
            self.root,
            placeholder_text="Username",
            width=250
        )
        self.new_username.pack(pady=10)
        self.new_password = ctk.CTkEntry(
            self.root,
            placeholder_text="Password",
            show="*",
            width=250
        )
        self.new_password.pack(pady=10)
        register_btn = ctk.CTkButton(
            self.root,
            text="Register",
            command=self.register
        )
        register_btn.pack(pady=20)
        back_btn = ctk.CTkButton(
            self.root,
            text="Back to Login",
            command=self.create_login_ui
        )
        back_btn.pack(pady=10)

    # ---------------- REGISTER FUNCTION ---------------- #
    def register(self):
        username = self.new_username.get()
        password = self.new_password.get()
        if username == "" or password == "":
            messagebox.showerror("Error", "All fields are required")
            return
        success = self.db.register_user(username, password)
        if success:
            messagebox.showinfo("Success", "Registration Successful")
            self.create_login_ui()
        else:
            messagebox.showerror("Error", "Username already exists")

    # ---------------- LOGIN FUNCTION ---------------- #
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user = self.db.login_user(username, password)
        if user:
            from Dashboard import Dashboard
            Dashboard(self.root)
        else:
            messagebox.showerror("Error", "Invalid Username or Password")

    # ---------------- CLEAR WINDOW ---------------- #
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
