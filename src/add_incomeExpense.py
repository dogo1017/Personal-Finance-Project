import customtkinter as ctk
import csv
import os

def get_expense_file(username):
    return f"docs/{username}/expenses.csv"

def initialize_file(username):
    path = get_expense_file(username)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not os.path.exists(path):
        with open(path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Type", "Date", "Amount", "Source", "Category"])

def add_entry(username, entry_type, date, amount, source, category):
    path = get_expense_file(username)
    with open(path, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([entry_type, date, amount, source, category])

def load_entries(username):
    path = get_expense_file(username)
    if not os.path.exists(path):
        return []
    with open(path, newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)

class IncomeExpenseFrame(ctk.CTkFrame):
    def __init__(self, parent, username):
        super().__init__(parent, corner_radius=0, fg_color="transparent")
        self.username = username
        initialize_file(username)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.build()

    def build(self):
        ctk.CTkLabel(self, text="Income & Expenses", font=("Arial", 26, "bold")).grid(
            row=0, column=0, columnspan=2, sticky="w", pady=(0, 16))

        self.build_add_panel()
        self.build_view_panel()

    def build_add_panel(self):
        panel = ctk.CTkFrame(self, corner_radius=12)
        panel.grid(row=1, column=0, sticky="nsew", padx=(0, 10))
        panel.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(panel, text="Add Entry", font=("Arial", 16, "bold")).grid(
            row=0, column=0, sticky="w", padx=20, pady=(16, 12))

        ctk.CTkLabel(panel, text="Type", font=("Arial", 12), text_color="#aaaaaa").grid(
            row=1, column=0, sticky="w", padx=20)
        self.type_var = ctk.StringVar(value="Income")
        ctk.CTkOptionMenu(panel, variable=self.type_var,
                          values=["Income", "Expense"], height=38, corner_radius=8).grid(
            row=2, column=0, sticky="ew", padx=20, pady=(4, 10))

        ctk.CTkLabel(panel, text="Date (YYYY-MM-DD)", font=("Arial", 12), text_color="#aaaaaa").grid(
            row=3, column=0, sticky="w", padx=20)
        self.date_entry = ctk.CTkEntry(panel, placeholder_text="e.g. 2024-03-15", height=38, corner_radius=8)
        self.date_entry.grid(row=4, column=0, sticky="ew", padx=20, pady=(4, 10))

        ctk.CTkLabel(panel, text="Amount ($)", font=("Arial", 12), text_color="#aaaaaa").grid(
            row=5, column=0, sticky="w", padx=20)
        self.amount_entry = ctk.CTkEntry(panel, placeholder_text="e.g. 250.00", height=38, corner_radius=8)
        self.amount_entry.grid(row=6, column=0, sticky="ew", padx=20, pady=(4, 10))

        ctk.CTkLabel(panel, text="Source", font=("Arial", 12), text_color="#aaaaaa").grid(
            row=7, column=0, sticky="w", padx=20)
        self.source_entry = ctk.CTkEntry(panel, placeholder_text="e.g. Job, Freelance", height=38, corner_radius=8)
        self.source_entry.grid(row=8, column=0, sticky="ew", padx=20, pady=(4, 10))

        ctk.CTkLabel(panel, text="Category", font=("Arial", 12), text_color="#aaaaaa").grid(
            row=9, column=0, sticky="w", padx=20)
        self.cat_var = ctk.StringVar(value="General")
        ctk.CTkOptionMenu(panel, variable=self.cat_var,
                          values=["General", "Food", "Rent", "Transport", "Entertainment",
                                  "Utilities", "Healthcare", "Savings", "Other"],
                          height=38, corner_radius=8).grid(
            row=10, column=0, sticky="ew", padx=20, pady=(4, 10))

        self.add_error = ctk.CTkLabel(panel, text="", font=("Arial", 11), text_color="#ff4444")
        self.add_error.grid(row=11, column=0, pady=(0, 4))

        self.add_result = ctk.CTkLabel(panel, text="", font=("Arial", 12), text_color="#2ecc71")
        self.add_result.grid(row=12, column=0, pady=(0, 4))

        ctk.CTkButton(panel, text="Add Entry", height=40, corner_radius=8,
                      font=("Arial", 13, "bold"),
                      command=self.submit_entry).grid(
            row=13, column=0, sticky="ew", padx=20, pady=(4, 20))

    def build_view_panel(self):
        panel = ctk.CTkFrame(self, corner_radius=12)
        panel.grid(row=1, column=1, sticky="nsew", padx=(10, 0))
        panel.grid_columnconfigure(0, weight=1)
        panel.grid_rowconfigure(5, weight=1)

        ctk.CTkLabel(panel, text="View Entries", font=("Arial", 16, "bold")).grid(
            row=0, column=0, sticky="w", padx=20, pady=(16, 12))

        ctk.CTkLabel(panel, text="Filter By", font=("Arial", 12), text_color="#aaaaaa").grid(
            row=1, column=0, sticky="w", padx=20)
        self.filter_var = ctk.StringVar(value="All")
        ctk.CTkOptionMenu(panel, variable=self.filter_var,
                          values=["All", "Income Only", "Expense Only", "By Date", "By Month"],
                          height=38, corner_radius=8).grid(
            row=2, column=0, sticky="ew", padx=20, pady=(4, 10))

        ctk.CTkLabel(panel, text="Filter Value (date or YYYY-MM)", font=("Arial", 12), text_color="#aaaaaa").grid(
            row=3, column=0, sticky="w", padx=20)
        self.filter_entry = ctk.CTkEntry(panel, placeholder_text="Leave blank for All", height=38, corner_radius=8)
        self.filter_entry.grid(row=4, column=0, sticky="ew", padx=20, pady=(4, 10))

        self.view_error = ctk.CTkLabel(panel, text="", font=("Arial", 11), text_color="#ff4444")
        self.view_error.grid(row=5, column=0)

        ctk.CTkButton(panel, text="Load Entries", height=38, corner_radius=8,
                      command=self.load_entries_view).grid(
            row=6, column=0, sticky="ew", padx=20, pady=(4, 10))

        self.results_box = ctk.CTkTextbox(panel, font=("Courier", 11), corner_radius=8)
        self.results_box.grid(row=7, column=0, sticky="nsew", padx=20, pady=(0, 20))
        self.results_box.configure(state="disabled")

        self.totals_label = ctk.CTkLabel(panel, text="", font=("Arial", 11), text_color="#aaaaaa")
        self.totals_label.grid(row=8, column=0, padx=20, pady=(0, 14))

    def submit_entry(self):
        self.add_error.configure(text="")
        self.add_result.configure(text="")
        entry_type = self.type_var.get()
        date = self.date_entry.get().strip()
        amount = self.amount_entry.get().strip()
        source = self.source_entry.get().strip()
        category = self.cat_var.get()

        if not date:
            self.add_error.configure(text="Date is required.")
            return
        parts = date.split("-")
        if len(parts) != 3 or not all(p.isdigit() for p in parts):
            self.add_error.configure(text="Date must be YYYY-MM-DD.")
            return
        if not amount:
            self.add_error.configure(text="Amount is required.")
            return
        try:
            float(amount)
        except ValueError:
            self.add_error.configure(text="Amount must be a number.")
            return
        if not source:
            self.add_error.configure(text="Source is required.")
            return

        add_entry(self.username, entry_type, date, amount, source, category)
        self.add_result.configure(text=f"{entry_type} of ${float(amount):.2f} added!")
        self.date_entry.delete(0, "end")
        self.amount_entry.delete(0, "end")
        self.source_entry.delete(0, "end")

    def load_entries_view(self):
        self.view_error.configure(text="")
        filter_type = self.filter_var.get()
        filter_val = self.filter_entry.get().strip()

        rows = load_entries(self.username)

        if filter_type == "Income Only":
            rows = [r for r in rows if r["Type"] == "Income"]
        elif filter_type == "Expense Only":
            rows = [r for r in rows if r["Type"] == "Expense"]
        elif filter_type == "By Date":
            if not filter_val:
                self.view_error.configure(text="Enter a date to filter by.")
                return
            rows = [r for r in rows if r["Date"] == filter_val]
        elif filter_type == "By Month":
            if not filter_val:
                self.view_error.configure(text="Enter a month (YYYY-MM) to filter by.")
                return
            parts = filter_val.split("-")
            if len(parts) != 2 or not all(p.isdigit() for p in parts) or not (1 <= int(parts[1]) <= 12):
                self.view_error.configure(text="Month must be YYYY-MM format.")
                return
            rows = [r for r in rows if r["Date"].startswith(filter_val)]

        self.results_box.configure(state="normal")
        self.results_box.delete("1.0", "end")

        if not rows:
            self.results_box.insert("end", "No entries found.")
            self.totals_label.configure(text="")
        else:
            self.results_box.insert("end", f"{'Type':<10} {'Date':<13} {'Amount':<10} {'Category':<14} Source\n")
            self.results_box.insert("end", "─" * 62 + "\n")
            total_in = 0.0
            total_out = 0.0
            for r in rows:
                amt = float(r["Amount"])
                if r["Type"] == "Income":
                    total_in += amt
                else:
                    total_out += amt
                self.results_box.insert("end",
                    f"{r['Type']:<10} {r['Date']:<13} ${amt:<9.2f} {r.get('Category',''):<14} {r.get('Source','')}\n")
            self.totals_label.configure(
                text=f"Income: ${total_in:,.2f}   Expenses: ${total_out:,.2f}   Net: ${total_in - total_out:,.2f}")

        self.results_box.configure(state="disabled")