import customtkinter as ctk

RATES = {
    "USD": 1.0,
    "EUR": 0.92,
    "GBP": 0.79,
    "JPY": 149.50,
    "CAD": 1.36,
    "MXN": 17.15,
}

CURRENCY_NAMES = {
    "USD": "US Dollar",
    "EUR": "Euro",
    "GBP": "British Pound",
    "JPY": "Japanese Yen",
    "CAD": "Canadian Dollar",
    "MXN": "Mexican Peso",
}

def convert(amount, from_currency, to_currency):
    in_usd = amount / RATES[from_currency]
    return in_usd * RATES[to_currency]

class CurrencyFrame(ctk.CTkFrame):
    def __init__(self, parent, username):
        super().__init__(parent, corner_radius=0, fg_color="transparent")
        self.username = username
        self.grid_columnconfigure(0, weight=1)
        self.build()

    def build(self):
        ctk.CTkLabel(self, text="Currency Converter", font=("Arial", 26, "bold")).grid(
            row=0, column=0, sticky="w", pady=(0, 20))

        card = ctk.CTkFrame(self, corner_radius=12)
        card.grid(row=1, column=0, sticky="n")
        card.grid_columnconfigure(0, weight=1)
        card.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(card, text="Amount", font=("Arial", 13), text_color="#aaaaaa").grid(
            row=0, column=0, columnspan=2, sticky="w", padx=30, pady=(24, 4))
        self.amount_entry = ctk.CTkEntry(card, placeholder_text="Enter amount", height=42,
                                         corner_radius=8, font=("Arial", 15), width=340)
        self.amount_entry.grid(row=1, column=0, columnspan=2, padx=30, pady=(0, 20), sticky="ew")

        ctk.CTkLabel(card, text="From", font=("Arial", 13), text_color="#aaaaaa").grid(
            row=2, column=0, sticky="w", padx=30, pady=(0, 4))
        ctk.CTkLabel(card, text="To", font=("Arial", 13), text_color="#aaaaaa").grid(
            row=2, column=1, sticky="w", padx=30, pady=(0, 4))

        currencies = list(RATES.keys())
        self.from_var = ctk.StringVar(value="USD")
        self.to_var = ctk.StringVar(value="EUR")

        ctk.CTkOptionMenu(card, variable=self.from_var, values=currencies,
                          height=40, corner_radius=8, width=150).grid(
            row=3, column=0, padx=(30, 10), pady=(0, 20), sticky="ew")

        ctk.CTkLabel(card, text="→", font=("Arial", 20)).grid(row=3, column=0, columnspan=2)

        ctk.CTkOptionMenu(card, variable=self.to_var, values=currencies,
                          height=40, corner_radius=8, width=150).grid(
            row=3, column=1, padx=(10, 30), pady=(0, 20), sticky="ew")

        self.convert_error = ctk.CTkLabel(card, text="", font=("Arial", 11), text_color="#ff4444")
        self.convert_error.grid(row=4, column=0, columnspan=2)

        ctk.CTkButton(card, text="Convert", height=42, corner_radius=8,
                      font=("Arial", 14, "bold"),
                      command=self.do_convert).grid(
            row=5, column=0, columnspan=2, sticky="ew", padx=30, pady=(8, 16))

        self.result_label = ctk.CTkLabel(card, text="", font=("Arial", 22, "bold"), text_color="#3498db")
        self.result_label.grid(row=6, column=0, columnspan=2, pady=(0, 8))

        self.detail_label = ctk.CTkLabel(card, text="", font=("Arial", 11), text_color="#888888")
        self.detail_label.grid(row=7, column=0, columnspan=2, pady=(0, 24))

        ctk.CTkLabel(card, text="Exchange Rates (relative to USD)",
                     font=("Arial", 13, "bold")).grid(row=8, column=0, columnspan=2, pady=(8, 8))

        rate_box = ctk.CTkTextbox(card, height=130, font=("Courier", 11), corner_radius=8, width=340)
        rate_box.grid(row=9, column=0, columnspan=2, padx=30, pady=(0, 24), sticky="ew")
        for code, rate in RATES.items():
            rate_box.insert("end", f"  {code}  {CURRENCY_NAMES[code]:<22}  1 USD = {rate:.4f} {code}\n")
        rate_box.configure(state="disabled")

    def do_convert(self):
        self.convert_error.configure(text="")
        self.result_label.configure(text="")
        self.detail_label.configure(text="")
        try:
            amount = float(self.amount_entry.get())
        except ValueError:
            self.convert_error.configure(text="Please enter a valid number.")
            return
        from_c = self.from_var.get()
        to_c = self.to_var.get()
        result = convert(amount, from_c, to_c)
        self.result_label.configure(text=f"{amount:,.2f} {from_c}  =  {result:,.2f} {to_c}")
        self.detail_label.configure(
            text=f"Rate: 1 {from_c} = {RATES[to_c] / RATES[from_c]:.4f} {to_c}  •  Rates are approximate")