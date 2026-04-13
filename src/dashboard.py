import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

NAV_ITEMS = [
    ("📊  Overview",       "overview"),
    ("💵  Income/Expense", "income"),
    ("📋  Budget",         "budget"),
    ("🎯  Savings Goal",   "savings"),
    ("📈  Charts",         "charts"),
    ("💱  Currency",       "currency"),
]

class Dashboard(ctk.CTk):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.title(f"FinanceTracker — {username}")
        self.geometry("1000x620")
        self.wm_minsize(800, 500)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.nav_buttons = {}
        self.active_section = "overview"

        self.build_sidebar()

        self.content = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.content.grid(row=0, column=1, sticky="nsew", padx=24, pady=24)
        self.content.grid_columnconfigure(0, weight=1)
        self.content.grid_rowconfigure(0, weight=1)

        self.show_section("overview")

    def build_sidebar(self):
        sidebar = ctk.CTkFrame(self, width=210, corner_radius=0)
        sidebar.grid(row=0, column=0, sticky="nsew")
        sidebar.grid_propagate(False)
        sidebar.grid_rowconfigure(len(NAV_ITEMS) + 2, weight=1)

        ctk.CTkLabel(sidebar, text="💰 FinanceTracker", font=("Arial", 16, "bold")).grid(
            row=0, column=0, padx=20, pady=(28, 6))
        ctk.CTkLabel(sidebar, text=f"@{self.username}", font=("Arial", 11),
                     text_color="#888888").grid(row=1, column=0, padx=20, pady=(0, 20))

        for idx, (label, key) in enumerate(NAV_ITEMS):
            btn = ctk.CTkButton(sidebar, text=label, width=170, height=38, anchor="w",
                                fg_color="transparent", text_color="white",
                                hover_color="#2a2d3e", corner_radius=8,
                                font=("Arial", 13),
                                command=lambda k=key: self.show_section(k))
            btn.grid(row=idx + 2, column=0, padx=18, pady=3)
            self.nav_buttons[key] = btn

        logout_btn = ctk.CTkButton(sidebar, text="⬅  Logout", width=170, height=36,
                                   fg_color="transparent", text_color="#ff6b6b",
                                   hover_color="#2a2d3e", anchor="w", corner_radius=8,
                                   font=("Arial", 12),
                                   command=self.logout)
        logout_btn.grid(row=len(NAV_ITEMS) + 3, column=0, padx=18, pady=(0, 24), sticky="s")

    def highlight_nav(self, key):
        for k, btn in self.nav_buttons.items():
            if k == key:
                btn.configure(fg_color="#1f538d")
            else:
                btn.configure(fg_color="transparent")

    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    def show_section(self, key):
        self.active_section = key
        self.highlight_nav(key)
        self.clear_content()

        if key == "overview":
            import overview
            overview.OverviewFrame(self.content, self.username).grid(row=0, column=0, sticky="nsew")

        elif key == "income":
            import add_incomeExpense
            add_incomeExpense.IncomeExpenseFrame(self.content, self.username).grid(row=0, column=0, sticky="nsew")

        elif key == "budget":
            import trues_file
            trues_file.BudgetFrame(self.content, self.username).grid(row=0, column=0, sticky="nsew")

        elif key == "savings":
            import trues_file
            trues_file.SavingsFrame(self.content, self.username).grid(row=0, column=0, sticky="nsew")

        elif key == "charts":
            import charts
            charts.ChartsFrame(self.content, self.username).grid(row=0, column=0, sticky="nsew")

        elif key == "currency":
            import currency
            currency.CurrencyFrame(self.content, self.username).grid(row=0, column=0, sticky="nsew")

    def logout(self):
        self.destroy()
        import entry
        entry.launch()