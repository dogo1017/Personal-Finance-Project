import customtkinter as ctk
import csv
import os

def get_file(username, filename):
    return f"docs/{username}/{filename}"

def ensure_file(path, headers):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not os.path.exists(path):
        with open(path, "w", newline="") as f:
            csv.writer(f).writerow(headers)

def load_csv_rows(path):
    if not os.path.exists(path):
        return []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)

class SavingsFrame(ctk.CTkFrame):
    def __init__(self, parent, username):
        super().__init__(parent, corner_radius=0, fg_color="transparent")
        self.username = username
        self.path = get_file(username, "savings.csv")
        ensure_file(self.path, ["Goal", "Monthly", "Months"])
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.build()

    def build(self):
        ctk.CTkLabel(self, text="Savings Goal Tracker", font=("Arial", 26, "bold")).grid(
            row=0, column=0, columnspan=2, sticky="w", pady=(0, 16))

        form = ctk.CTkFrame(self, corner_radius=12)
        form.grid(row=1, column=0, sticky="nsew", padx=(0, 10))
        form.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(form, text="Set New Savings Goal", font=("Arial", 16, "bold")).grid(
            row=0, column=0, sticky="w", padx=20, pady=(16, 12))

        ctk.CTkLabel(form, text="Savings Goal Amount ($)", font=("Arial", 12), text_color="#aaaaaa").grid(
            row=1, column=0, sticky="w", padx=20)
        self.goal_entry = ctk.CTkEntry(form, placeholder_text="e.g. 5000", height=38, corner_radius=8)
        self.goal_entry.grid(row=2, column=0, sticky="ew", padx=20, pady=(4, 12))

        ctk.CTkLabel(form, text="Monthly Savings Amount ($)", font=("Arial", 12), text_color="#aaaaaa").grid(
            row=3, column=0, sticky="w", padx=20)
        self.monthly_entry = ctk.CTkEntry(form, placeholder_text="e.g. 200", height=38, corner_radius=8)
        self.monthly_entry.grid(row=4, column=0, sticky="ew", padx=20, pady=(4, 12))

        self.save_error = ctk.CTkLabel(form, text="", font=("Arial", 11), text_color="#ff4444")
        self.save_error.grid(row=5, column=0)

        self.save_result = ctk.CTkLabel(form, text="", font=("Arial", 12), text_color="#2ecc71", wraplength=280)
        self.save_result.grid(row=6, column=0, padx=20)

        ctk.CTkButton(form, text="Calculate & Save Goal", height=40, corner_radius=8,
                      font=("Arial", 13, "bold"),
                      command=self.calculate_savings).grid(
            row=7, column=0, sticky="ew", padx=20, pady=(12, 20))

        history_panel = ctk.CTkFrame(self, corner_radius=12)
        history_panel.grid(row=1, column=1, sticky="nsew", padx=(10, 0))
        history_panel.grid_columnconfigure(0, weight=1)
        history_panel.grid_rowconfigure(2, weight=1)

        ctk.CTkLabel(history_panel, text="Saved Goals", font=("Arial", 16, "bold")).grid(
            row=0, column=0, sticky="w", padx=20, pady=(16, 12))

        self.history_box = ctk.CTkTextbox(history_panel, font=("Courier", 11), corner_radius=8)
        self.history_box.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 10))
        self.history_box.configure(state="disabled")

        ctk.CTkButton(history_panel, text="Refresh Goals", height=36, corner_radius=8,
                      command=self.load_history).grid(
            row=2, column=0, sticky="ew", padx=20, pady=(0, 20))

        self.load_history()

    def calculate_savings(self):
        self.save_error.configure(text="")
        self.save_result.configure(text="")
        try:
            savings_amount = float(self.goal_entry.get())
            monthly = float(self.monthly_entry.get())
            if monthly <= 0:
                self.save_error.configure(text="Monthly savings must be greater than 0.")
                return
            length = savings_amount / monthly
            self.save_result.configure(
                text=f"It will take {length:.1f} months ({length/12:.1f} years) to reach your ${savings_amount:,.2f} goal.")
            with open(self.path, "a", newline="") as f:
                csv.writer(f).writerow([savings_amount, monthly, round(length, 2)])
            self.load_history()
            self.goal_entry.delete(0, "end")
            self.monthly_entry.delete(0, "end")
        except ValueError:
            self.save_error.configure(text="Please enter valid numbers.")

    def load_history(self):
        rows = load_csv_rows(self.path)
        self.history_box.configure(state="normal")
        self.history_box.delete("1.0", "end")
        if not rows:
            self.history_box.insert("end", "No saved goals yet.")
        else:
            self.history_box.insert("end", f"{'Goal ($)':<14} {'Monthly ($)':<14} Months\n")
            self.history_box.insert("end", "─" * 40 + "\n")
            for r in rows:
                self.history_box.insert("end",
                    f"${float(r['Goal']):<13,.2f} ${float(r['Monthly']):<13,.2f} {r['Months']}\n")
        self.history_box.configure(state="disabled")


class BudgetFrame(ctk.CTkFrame):
    def __init__(self, parent, username):
        super().__init__(parent, corner_radius=0, fg_color="transparent")
        self.username = username
        self.path = get_file(username, "budget.csv")
        ensure_file(self.path, ["Category", "Limit", "Expenses"])
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.build()

    def build(self):
        ctk.CTkLabel(self, text="Budget Manager", font=("Arial", 26, "bold")).grid(
            row=0, column=0, columnspan=2, sticky="w", pady=(0, 16))

        form = ctk.CTkFrame(self, corner_radius=12)
        form.grid(row=1, column=0, sticky="nsew", padx=(0, 10))
        form.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(form, text="Set Budget Limit", font=("Arial", 16, "bold")).grid(
            row=0, column=0, sticky="w", padx=20, pady=(16, 12))

        ctk.CTkLabel(form, text="Category", font=("Arial", 12), text_color="#aaaaaa").grid(
            row=1, column=0, sticky="w", padx=20)
        self.cat_var = ctk.StringVar(value="Food")
        ctk.CTkOptionMenu(form, variable=self.cat_var,
                          values=["Food", "Rent", "Transport", "Entertainment",
                                  "Utilities", "Healthcare", "Savings", "General", "Other"],
                          height=38, corner_radius=8).grid(
            row=2, column=0, sticky="ew", padx=20, pady=(4, 12))

        ctk.CTkLabel(form, text="Budget Limit ($)", font=("Arial", 12), text_color="#aaaaaa").grid(
            row=3, column=0, sticky="w", padx=20)
        self.limit_entry = ctk.CTkEntry(form, placeholder_text="e.g. 500", height=38, corner_radius=8)
        self.limit_entry.grid(row=4, column=0, sticky="ew", padx=20, pady=(4, 12))

        ctk.CTkLabel(form, text="Actual Expenses ($)", font=("Arial", 12), text_color="#aaaaaa").grid(
            row=5, column=0, sticky="w", padx=20)
        self.expense_entry = ctk.CTkEntry(form, placeholder_text="e.g. 350", height=38, corner_radius=8)
        self.expense_entry.grid(row=6, column=0, sticky="ew", padx=20, pady=(4, 12))

        self.budget_error = ctk.CTkLabel(form, text="", font=("Arial", 11), text_color="#ff4444")
        self.budget_error.grid(row=7, column=0)

        self.budget_result = ctk.CTkLabel(form, text="", font=("Arial", 12), wraplength=280)
        self.budget_result.grid(row=8, column=0, padx=20)

        ctk.CTkButton(form, text="Save Budget", height=40, corner_radius=8,
                      font=("Arial", 13, "bold"),
                      command=self.save_budget).grid(
            row=9, column=0, sticky="ew", padx=20, pady=(12, 20))

        history_panel = ctk.CTkFrame(self, corner_radius=12)
        history_panel.grid(row=1, column=1, sticky="nsew", padx=(10, 0))
        history_panel.grid_columnconfigure(0, weight=1)
        history_panel.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(history_panel, text="Budget vs Expenses", font=("Arial", 16, "bold")).grid(
            row=0, column=0, sticky="w", padx=20, pady=(16, 12))

        self.history_box = ctk.CTkTextbox(history_panel, font=("Courier", 11), corner_radius=8)
        self.history_box.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 10))
        self.history_box.configure(state="disabled")

        ctk.CTkButton(history_panel, text="Refresh", height=36, corner_radius=8,
                      command=self.load_history).grid(
            row=2, column=0, sticky="ew", padx=20, pady=(0, 20))

        self.load_history()

    def save_budget(self):
        self.budget_error.configure(text="")
        self.budget_result.configure(text="")
        try:
            limit = float(self.limit_entry.get())
            expenses = float(self.expense_entry.get())
            category = self.cat_var.get()
            with open(self.path, "a", newline="") as f:
                csv.writer(f).writerow([category, limit, expenses])
            remaining = limit - expenses
            if remaining >= 0:
                self.budget_result.configure(
                    text=f"Saved! ${remaining:,.2f} remaining under budget.", text_color="#2ecc71")
            else:
                self.budget_result.configure(
                    text=f"Saved! Over budget by ${abs(remaining):,.2f}.", text_color="#e74c3c")
            self.load_history()
            self.limit_entry.delete(0, "end")
            self.expense_entry.delete(0, "end")
        except ValueError:
            self.budget_error.configure(text="Please enter valid numbers.")

    def load_history(self):
        rows = load_csv_rows(self.path)
        self.history_box.configure(state="normal")
        self.history_box.delete("1.0", "end")
        if not rows:
            self.history_box.insert("end", "No budget entries yet.")
        else:
            self.history_box.insert("end", f"{'Category':<14} {'Limit ($)':<12} {'Spent ($)':<12} Status\n")
            self.history_box.insert("end", "─" * 52 + "\n")
            for r in rows:
                limit = float(r["Limit"])
                spent = float(r["Expenses"])
                status = "✓ Under" if spent <= limit else "✗ Over"
                self.history_box.insert("end",
                    f"{r['Category']:<14} ${limit:<11,.2f} ${spent:<11,.2f} {status}\n")
        self.history_box.configure(state="disabled")