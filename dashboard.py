import customtkinter as ctk
from database import Database
from reminders import ReminderSystem

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.db = Database()
        self.reminder = ReminderSystem()
        self.create_dashboard()

    # ---------------- DASHBOARD UI ---------------- #
    def create_dashboard(self):
        self.clear_window()
        # Sidebar
        sidebar = ctk.CTkFrame(
            self.root,
            width=200,
            corner_radius=0
        )
        sidebar.pack(side="left", fill="y")
        # Title
        title = ctk.CTkLabel(
            sidebar,
            text="Interview Tracker",
            font=("Arial", 22, "bold")
        )
        title.pack(pady=30)
        # Dashboard Button
        dashboard_btn = ctk.CTkButton(
            sidebar,
            text="Dashboard"
        )
        dashboard_btn.pack(pady=10)
        # Topics Button
        topics_btn = ctk.CTkButton(
            sidebar,
            text="Topics",
            command=self.open_topics
        )
        topics_btn.pack(pady=10)
        # Analytics Button
        analytics_btn = ctk.CTkButton(
            sidebar,
            text="Analytics",
            command=self.open_analytics
        )
        analytics_btn.pack(pady=10)
        # Study Logs Button
        study_btn = ctk.CTkButton(
            sidebar,
            text="Study Logs",
            command=self.open_study_logs
        )
        study_btn.pack(pady=10)
        # Company Tracker Button
        company_btn = ctk.CTkButton(
            sidebar,
            text="Company Tracker",
            command=self.open_company_tracker
        )
        company_btn.pack(pady=10)
        # Mock Interviews Button
        mock_btn = ctk.CTkButton(
            sidebar,
            text="Mock Interviews",
            command=self.open_mock_interviews
        )
        mock_btn.pack(pady=10)
        # Reminders Button
        reminder_btn = ctk.CTkButton(
            sidebar,
            text="Check Reminders",
            command=self.reminder.check_pending_topics
        )
        reminder_btn.pack(pady=10)
        # Main Content
        content = ctk.CTkFrame(self.root)
        content.pack(
            side="right",
            expand=True,
            fill="both"
        )
        # Heading
        heading = ctk.CTkLabel(
            content,
            text="Dashboard",
            font=("Arial", 30, "bold")
        )
        heading.pack(pady=20)
        # Dashboard Cards
        cards_frame = ctk.CTkFrame(content)
        cards_frame.pack(pady=20)
        topics = self.db.get_topics()
        total_topics = len(topics)
        completed_topics = len(
            [topic for topic in topics if topic[4] == "Completed"]
        )
        pending_topics = len(
            [topic for topic in topics if topic[4] == "Pending"]
        )
        # Total Topics Card
        total_card = ctk.CTkFrame(
            cards_frame,
            width=180,
            height=120
        )
        total_card.grid(
            row=0,
            column=0,
            padx=15
        )
        total_label = ctk.CTkLabel(
            total_card,
            text=f"Total Topics\n{total_topics}",
            font=("Arial", 20, "bold")
        )
        total_label.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )
        # Completed Card
        completed_card = ctk.CTkFrame(
            cards_frame,
            width=180,
            height=120
        )
        completed_card.grid(
            row=0,
            column=1,
            padx=15
        )
        completed_label = ctk.CTkLabel(
            completed_card,
            text=f"Completed\n{completed_topics}",
            font=("Arial", 20, "bold")
        )
        completed_label.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )
        # Pending Card
        pending_card = ctk.CTkFrame(
            cards_frame,
            width=180,
            height=120
        )
        pending_card.grid(
            row=0,
            column=2,
            padx=15
        )
        pending_label = ctk.CTkLabel(
            pending_card,
            text=f"Pending\n{pending_topics}",
            font=("Arial", 20, "bold")
        )
        pending_label.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

    # ---------------- OPEN TOPICS ---------------- #
    def open_topics(self):
        from topic_manager import TopicManager
        TopicManager(self.root)

    # ---------------- OPEN ANALYTICS ---------------- #
    def open_analytics(self):
        from analytics import AnalyticsPage
        AnalyticsPage(self.root)

    # ---------------- OPEN STUDY LOGS ---------------- #
    def open_study_logs(self):
        from study_log import StudyLogPage
        StudyLogPage(self.root)

    # ---------------- OPEN COMPANY TRACKER ---------------- #
    def open_company_tracker(self):
        from company_tracker import CompanyTrackerPage
        CompanyTrackerPage(self.root)

    # ---------------- OPEN MOCK INTERVIEWS ---------------- #
    def open_mock_interviews(self):
        pass

    # ---------------- CLEAR WINDOW ---------------- #
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
