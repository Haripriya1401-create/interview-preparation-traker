import customtkinter as ctk
from database import Database
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class AnalyticsPage:
    def __init__(self, root):
        self.root = root
        self.db = Database()
        self.create_analytics_ui()

    # ---------------- ANALYTICS UI ---------------- #
    def create_analytics_ui(self):
        self.clear_window()
        heading = ctk.CTkLabel(
            self.root,
            text="Analytics Dashboard",
            font=("Arial", 30, "bold")
        )
        heading.pack(pady=20)
        topics = self.db.get_topics()
        completed = len(
            [topic for topic in topics if topic[4] == "Completed"]
        )
        pending = len(
            [topic for topic in topics if topic[4] == "Pending"]
        )
        # Chart Frame
        chart_frame = ctk.CTkFrame(self.root)
        chart_frame.pack(pady=20, fill="both", expand=True)
        # Matplotlib Figure
        figure = plt.Figure(figsize=(5, 5), dpi=100)
        ax = figure.add_subplot(111)
        labels = ["Completed", "Pending"]
        values = [completed, pending]
        ax.pie(
            values,
            labels=labels,
            autopct="%1.1f%%"
        )
        ax.set_title("Interview Preparation Progress")
        # Display Chart
        canvas = FigureCanvasTkAgg(
            figure,
            master=chart_frame
        )
        canvas.draw()
        canvas.get_tk_widget().pack(
            fill="both",
            expand=True
        )

    # ---------------- CLEAR WINDOW ---------------- #
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
