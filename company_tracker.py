import customtkinter as ctk
from tkinter import ttk, messagebox
from database import Database

class CompanyTrackerPage:
    def __init__(self, root):
        self.root = root
        self.db = Database()
        self.create_company_ui()

    # ---------------- UI ---------------- #
    def create_company_ui(self):
        self.clear_window()
        heading = ctk.CTkLabel(
            self.root,
            text="Company Preparation Tracker",
            font=("Arial", 28, "bold")
        )
        heading.pack(pady=20)
        # Company Name
        self.company_entry = ctk.CTkEntry(
            self.root,
            placeholder_text="Company Name",
            width=250
        )
        self.company_entry.pack(pady=10)
        # Topic
        self.topic_entry = ctk.CTkEntry(
            self.root,
            placeholder_text="Preparation Topic",
            width=250
        )
        self.topic_entry.pack(pady=10)
        # Status
        self.status_option = ctk.CTkOptionMenu(
            self.root,
            values=["Pending", "Completed"]
        )
        self.status_option.pack(pady=10)
        # Add Button
        add_btn = ctk.CTkButton(
            self.root,
            text="Add Company Topic",
            command=self.add_company_topic
        )
        add_btn.pack(pady=20)
        # Table
        self.tree = ttk.Treeview(
            self.root,
            columns=("ID", "Company", "Topic", "Status"),
            show="headings",
            height=10
        )
        self.tree.heading("ID", text="ID")
        self.tree.heading("Company", text="Company")
        self.tree.heading("Topic", text="Topic")
        self.tree.heading("Status", text="Status")
        self.tree.pack(pady=20)
        self.load_company_topics()

    # ---------------- ADD COMPANY TOPIC ---------------- #
    def add_company_topic(self):
        company = self.company_entry.get()
        topic = self.topic_entry.get()
        status = self.status_option.get()
        if company == "" or topic == "":
            messagebox.showerror(
                "Error",
                "All fields are required"
            )
            return
        self.db.add_company_topic(
            company,
            topic,
            status
        )
        messagebox.showinfo(
            "Success",
            "Company Topic Added"
        )
        self.load_company_topics()

    # ---------------- LOAD DATA ---------------- #
    def load_company_topics(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        data = self.db.get_company_topics()
        for item in data:
            self.tree.insert(
                "",
                "end",
                values=item
            )

    # ---------------- CLEAR WINDOW ---------------- #
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
