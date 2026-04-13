import customtkinter as ctk
import csv
import os

def get_user_file(username, filename):
    return f"docs/{username}/{filename}"

def load_expenses(username):
    path = get_user_file(username, "expenses.csv")
    if not os.path.exists(path):
        return []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)

def load_savings(username):
    path = get_user_file(username, "savings.csv")
    if not os.path.exists(path):
        return []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)

def load_budget(username):
    path = get_user_file(username, "budget.csv")
    if not os.path.exists(path):
        return []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)

class OverviewFrame(ctk.CTkFrame):
    def __init__(self, parent, username):
        super().__init__(parent, corner_radius=0, fg_color="transparent")
        self.username = username
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.build()

    def build(self):
        ctk.CTkLabel(self, text="Overview", font=("Arial", 26, "bold")).grid(
            row=0, column=0, columnspan=3, sticky="w", pady=(0, 20))

        rows = load_expenses(self.username)
        total_income = sum(float(r["Amount"]) for r in rows if r["Type"] == "Income")
        total_expense = sum(float(r["Amount"]) for r in rows if r["Type"] == "Expense")
        net = total_income - total_expense

        self.stat_card("💵 Total Income", f"${total_income:,.2f}", "#2ecc71", 1, 0)
        self.stat_card("🧾 Total Expenses", f"${total_expense:,.2f}", "#e74c3c", 1, 1)
        net_color = "#2ecc71" if net >= 0 else "#e74c3c"
        self.stat_card("📊 Net Balance", f"${net:,.2f}", net_color, 1, 2)

        savings_rows = load_savings(self.username)
        budget_rows = load_budget(self.username)

        info_frame = ctk.CTkFrame(self, corner_radius=12)
        info_frame.grid(row=2, column=0, columnspan=3, sticky="nsew", pady=(20, 0))
        info_frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(info_frame, text="Recent Activity", font=("Arial", 15, "bold")).grid(
            row=0, column=0, sticky="w", padx=20, pady=(16, 8))

        box = ctk.CTkTextbox(info_frame, height=200, font=("Courier", 12), corner_radius=8)
        box.grid(row=1, column=0, sticky="ew", padx=20, pady=(0, 16))

        if rows:
            recent = rows[-8:]
            recent.reverse()
            box.insert("end", f"{'Type':<10} {'Date':<13} {'Amount':<12} {'Source/Category'}\n")
            box.insert("end", "─" * 55 + "\n")
            for r in recent:
                box.insert("end", f"{r['Type']:<10} {r['Date']:<13} ${float(r['Amount']):<11.2f} {r.get('Source', r.get('Category', ''))}\n")
        else:
            box.insert("end", "No entries yet. Add income or expenses to get started.")
        box.configure(state="disabled")

        savings_count = len(savings_rows)
        budget_count = len(budget_rows)
        ctk.CTkLabel(info_frame,
                     text=f"  📁 {len(rows)} total entries   •   🎯 {savings_count} savings goal(s)   •   📋 {budget_count} budget limit(s)",
                     font=("Arial", 11), text_color="#888888").grid(row=2, column=0, sticky="w", padx=20, pady=(0, 14))

    def stat_card(self, label, value, color, row, col):
        card = ctk.CTkFrame(self, corner_radius=12)
        card.grid(row=row, column=col, sticky="nsew", padx=6, pady=4)
        card.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(card, text=label, font=("Arial", 12), text_color="#aaaaaa").grid(
            row=0, column=0, padx=20, pady=(16, 4))
        ctk.CTkLabel(card, text=value, font=("Arial", 22, "bold"), text_color=color).grid(
            row=1, column=0, padx=20, pady=(0, 16))