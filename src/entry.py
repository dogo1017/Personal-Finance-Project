import customtkinter as ctk
import login
import user_registration

MIN_PASSWORD_LENGTH = 5
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

class LoginApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Personal Finance Tracker")
        self.geometry("420x480")
        self.wm_minsize(320, 380)
        self.resizable(True, True)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.current_mode = "login"
        self.error_labels = []

        self.frame = ctk.CTkFrame(self, corner_radius=16)
        self.frame.pack(expand=True, fill="both", padx=30, pady=30)
        self.frame.grid_columnconfigure(0, weight=1)

        self.render_screen()

    def clear_errors(self):
        for label in self.error_labels:
            label.destroy()
        self.error_labels.clear()

    def show_error(self, text, row):
        lbl = ctk.CTkLabel(self.frame, text=text, text_color="#ff4444", font=("Arial", 11))
        lbl.grid(row=row, column=0, pady=(0, 4))
        self.error_labels.append(lbl)

    def toggle_mode(self):
        self.current_mode = "signup" if self.current_mode == "login" else "login"
        self.render_screen()

    def handle_submit(self, user_ent, pass_ent):
        self.clear_errors()
        username = user_ent.get().strip()
        password = pass_ent.get()
        has_error = False

        if not username:
            self.show_error("Username required", 2)
            has_error = True

        if not password:
            self.show_error("Password required", 4)
            has_error = True
        elif len(password) < MIN_PASSWORD_LENGTH:
            self.show_error(f"Password must be at least {MIN_PASSWORD_LENGTH} characters", 4)
            has_error = True
        if has_error:
            return

        if self.current_mode == "login":
            if login.log_in(username, password):
                user_registration.init_user_folder(username)
                self.destroy()
                import dashboard
                dash = dashboard.Dashboard(username)
                dash.mainloop()
            else:
                self.show_error("Invalid username or password", 7)
        else:
            if user_registration.username_exists(username):
                self.show_error("Username already taken", 2)
            else:
                updated = user_registration.register(user_registration.load_csv(), password, username)
                user_registration.save_changes(updated)
                user_registration.init_user_folder(username)
                self.toggle_mode()

    def render_screen(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.clear_errors()

        title_text = "Welcome Back" if self.current_mode == "login" else "Create Account"
        subtitle = "Sign in to your account" if self.current_mode == "login" else "Set up your profile"
        btn_text = "Login" if self.current_mode == "login" else "Sign Up"
        toggle_text = "New here? Create an account" if self.current_mode == "login" else "Already have an account? Login"

        ctk.CTkLabel(self.frame, text="💰 FinanceTracker", font=("Arial", 14), text_color="#aaaaaa").grid(row=0, column=0, pady=(20, 0))
        ctk.CTkLabel(self.frame, text=title_text, font=("Arial", 26, "bold")).grid(row=1, column=0, pady=(4, 2))
        ctk.CTkLabel(self.frame, text=subtitle, font=("Arial", 12), text_color="#888888").grid(row=2, column=0, pady=(0, 18))

        entry_user = ctk.CTkEntry(self.frame, placeholder_text="Username", width=270, height=42, corner_radius=10)
        entry_user.grid(row=3, column=0, pady=6)

        entry_pass = ctk.CTkEntry(self.frame, placeholder_text="Password", show="*", width=270, height=42, corner_radius=10)
        entry_pass.grid(row=5, column=0, pady=6)

        ctk.CTkButton(self.frame, text=btn_text, width=270, height=42, corner_radius=10,
                      font=("Arial", 14, "bold"),
                      command=lambda: self.handle_submit(entry_user, entry_pass)).grid(row=8, column=0, pady=20)

        ctk.CTkButton(self.frame, text=toggle_text, fg_color="transparent",
                      text_color="#5b9bd5", hover=False, command=self.toggle_mode,
                      font=("Arial", 11)).grid(row=9, column=0, pady=(0, 10))

def launch():
    app = LoginApp()
    app.mainloop()