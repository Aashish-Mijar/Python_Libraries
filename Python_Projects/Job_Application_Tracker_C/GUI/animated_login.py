import tkinter as tk
from tkinter import messagebox
import itertools
from Database import auth
from GUI.main_window import JobAppTrackerGUI

class AnimatedLogin:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Job Tracker Login")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        # Gradient canvas
        self.canvas = tk.Canvas(self.root, width=600, height=400, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Color cycle
        self.colors = itertools.cycle([
            ("#ff6b6b", "#ffd93d"),
            ("#6bcB77", "#4D96FF"),
            ("#9D4EDD", "#FF6F91"),
            ("#06D6A0", "#118AB2"),
            ("#F72585", "#7209B7")
        ])
        self.current_colors = next(self.colors)

        # Login frame
        self.frame = tk.Frame(self.canvas, bg="white", bd=0, relief="flat")
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(self.frame, text="Login", font=("Arial", 18, "bold"), bg="white").pack(pady=10)

        tk.Label(self.frame, text="Username", bg="white").pack(pady=5)
        self.username_entry = tk.Entry(self.frame, width=30)
        self.username_entry.pack(pady=5)

        tk.Label(self.frame, text="Password", bg="white").pack(pady=5)
        self.password_entry = tk.Entry(self.frame, show="*", width=30)
        self.password_entry.pack(pady=5)

        tk.Button(self.frame, text="Login", command=self.login).pack(pady=10)
        tk.Button(self.frame, text="Sign Up", command=self.sign_up).pack(pady=5)

        # Start gradient animation
        self.animate_gradient()

    def draw_gradient(self, color1, color2):
        """Draw vertical gradient"""
        self.canvas.delete("gradient")
        steps = 100
        r1, g1, b1 = self.root.winfo_rgb(color1)
        r2, g2, b2 = self.root.winfo_rgb(color2)

        r_ratio = (r2 - r1) / steps
        g_ratio = (g2 - g1) / steps
        b_ratio = (b2 - b1) / steps

        for i in range(steps):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            hex_color = f"#{nr//256:02x}{ng//256:02x}{nb//256:02x}"
            self.canvas.create_rectangle(0, (400/steps)*i, 600, (400/steps)*(i+1),
                                         outline="", fill=hex_color, tags="gradient")

    def animate_gradient(self):
        next_colors = next(self.colors)
        self.draw_gradient(*next_colors)
        self.root.after(5000, self.animate_gradient)  # change every 5s

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if auth.verify_user(username, password):
            messagebox.showinfo("Success", "Login Successful!")
            from Database.auth import get_user_id
            user_id = auth.get_user_id(username)

            self.root.destroy()
            app = JobAppTrackerGUI(user_id)
            app.run()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def sign_up(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if auth.register_user(username, password):
            messagebox.showinfo("Success", "User registered successfully!")
        else:
            messagebox.showerror("Error", "Username already exists")

    def run(self):
        self.root.mainloop()
