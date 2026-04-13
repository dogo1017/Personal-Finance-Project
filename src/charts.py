import customtkinter as ctk
import csv
import os
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def load_entries(username):
    path = f"docs/{username}/expenses.csv"
    if not os.path.exists(path):
        return []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)

class ChartsFrame(ctk.CTkFrame):
    def __init__(self, parent, username):
        super().__init__(parent, corner_radius=0, fg_color="transparent")
        self.username = username
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.canvas_widget = None
        self.build()

    def build(self):
        ctk.CTkLabel(self, text="Charts & Visualizations", font=("Arial", 26, "bold")).grid(
            row=0, column=0, sticky="w", pady=(0, 16))

        controls = ctk.CTkFrame(self, corner_radius=12, height=60)
        controls.grid(row=1, column=0, sticky="ew", pady=(0, 12))
        controls.grid_columnconfigure(2, weight=1)

        ctk.CTkLabel(controls, text="Chart Type", font=("Arial", 12), text_color="#aaaaaa").grid(
            row=0, column=0, padx=(20, 8), pady=14)
        self.chart_var = ctk.StringVar(value="Expenses by Category (Pie)")
        ctk.CTkOptionMenu(controls, variable=self.chart_var,
                          values=["Expenses by Category (Pie)",
                                  "Income vs Expense by Month (Bar)",
                                  "Spending Trend (Line)"],
                          width=260, height=36, corner_radius=8).grid(
            row=0, column=1, padx=8, pady=14)

        ctk.CTkButton(controls, text="Generate Chart", height=36, corner_radius=8,
                      width=150, font=("Arial", 13, "bold"),
                      command=self.generate_chart).grid(
            row=0, column=2, padx=20, pady=14, sticky="e")

        self.chart_area = ctk.CTkFrame(self, corner_radius=12)
        self.chart_area.grid(row=2, column=0, sticky="nsew")
        self.chart_area.grid_columnconfigure(0, weight=1)
        self.chart_area.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.msg_label = ctk.CTkLabel(self.chart_area,
                                      text="Select a chart type and click Generate.",
                                      font=("Arial", 13), text_color="#888888")
        self.msg_label.grid(row=0, column=0, pady=40)

    def clear_chart(self):
        if self.canvas_widget:
            self.canvas_widget.get_tk_widget().destroy()
            self.canvas_widget = None
        self.msg_label.grid(row=0, column=0, pady=40)

    def show_chart(self, fig):
        self.msg_label.grid_forget()
        canvas = FigureCanvasTkAgg(fig, master=self.chart_area)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.canvas_widget = canvas

    def generate_chart(self):
        self.clear_chart()
        rows = load_entries(self.username)
        chart_type = self.chart_var.get()

        plt.style.use("dark_background")

        if chart_type == "Expenses by Category (Pie)":
            self.pie_chart(rows)
        elif chart_type == "Income vs Expense by Month (Bar)":
            self.bar_chart(rows)
        elif chart_type == "Spending Trend (Line)":
            self.line_chart(rows)

    def pie_chart(self, rows):
        expenses = [r for r in rows if r["Type"] == "Expense"]
        if not expenses:
            self.msg_label.configure(text="No expense entries found.")
            return

        category_totals = {}
        for r in expenses:
            cat = r.get("Category", "General")
            category_totals[cat] = category_totals.get(cat, 0) + float(r["Amount"])

        fig = Figure(figsize=(6, 5), facecolor="#1a1a2e")
        ax = fig.add_subplot(111)
        ax.set_facecolor("#1a1a2e")

        colors = ["#3498db","#e74c3c","#2ecc71","#f39c12","#9b59b6","#1abc9c","#e67e22","#e91e63"]
        wedges, texts, autotexts = ax.pie(
            list(category_totals.values()),
            labels=list(category_totals.keys()),
            autopct="%1.1f%%",
            colors=colors[:len(category_totals)],
            textprops={"color": "white", "fontsize": 10}
        )
        for at in autotexts:
            at.set_fontsize(9)
        ax.set_title("Expenses by Category", color="white", fontsize=14, pad=16)
        fig.tight_layout()
        self.show_chart(fig)

    def bar_chart(self, rows):
        if not rows:
            self.msg_label.configure(text="No entries found.")
            return

        month_income = {}
        month_expense = {}
        for r in rows:
            month = r["Date"][:7]
            amt = float(r["Amount"])
            if r["Type"] == "Income":
                month_income[month] = month_income.get(month, 0) + amt
            else:
                month_expense[month] = month_expense.get(month, 0) + amt

        all_months = sorted(set(list(month_income.keys()) + list(month_expense.keys())))
        income_vals = [month_income.get(m, 0) for m in all_months]
        expense_vals = [month_expense.get(m, 0) for m in all_months]

        fig = Figure(figsize=(6, 5), facecolor="#1a1a2e")
        ax = fig.add_subplot(111)
        ax.set_facecolor("#1a1a2e")

        x = range(len(all_months))
        bar_width = 0.35
        ax.bar([i - bar_width/2 for i in x], income_vals, width=bar_width, label="Income", color="#2ecc71")
        ax.bar([i + bar_width/2 for i in x], expense_vals, width=bar_width, label="Expenses", color="#e74c3c")
        ax.set_xticks(list(x))
        ax.set_xticklabels(all_months, rotation=30, ha="right", color="white", fontsize=9)
        ax.tick_params(colors="white")
        ax.set_title("Income vs Expenses by Month", color="white", fontsize=14)
        ax.set_ylabel("Amount ($)", color="white")
        ax.legend(facecolor="#2a2d3e", labelcolor="white")
        for spine in ax.spines.values():
            spine.set_edgecolor("#444")
        fig.tight_layout()
        self.show_chart(fig)

    def line_chart(self, rows):
        if not rows:
            self.msg_label.configure(text="No entries found.")
            return

        month_expense = {}
        for r in rows:
            if r["Type"] == "Expense":
                month = r["Date"][:7]
                month_expense[month] = month_expense.get(month, 0) + float(r["Amount"])

        if not month_expense:
            self.msg_label.configure(text="No expense entries found.")
            return

        months = sorted(month_expense.keys())
        totals = [month_expense[m] for m in months]

        fig = Figure(figsize=(6, 5), facecolor="#1a1a2e")
        ax = fig.add_subplot(111)
        ax.set_facecolor("#1a1a2e")

        ax.plot(months, totals, color="#3498db", linewidth=2.5, marker="o", markersize=7, markerfacecolor="white")
        ax.fill_between(range(len(months)), totals, alpha=0.15, color="#3498db")
        ax.set_xticks(range(len(months)))
        ax.set_xticklabels(months, rotation=30, ha="right", color="white", fontsize=9)
        ax.tick_params(colors="white")
        ax.set_title("Monthly Spending Trend", color="white", fontsize=14)
        ax.set_ylabel("Total Expenses ($)", color="white")
        for spine in ax.spines.values():
            spine.set_edgecolor("#444")
        fig.tight_layout()
        self.show_chart(fig)