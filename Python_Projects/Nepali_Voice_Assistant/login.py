import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import itertools
import app  # import your main assistant

# ---------- Animated Login Window ----------
class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Nepali Voice Assistant - Login")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        # ---- Background Image ----
        self.bg_img = Image.open("assets/bg.png").resize((600, 400))
        self.bg_photo = ImageTk.PhotoImage(self.bg_img)
        self.bg_label = tk.Label(root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # ---- Title Animation ----
        self.colors = itertools.cycle(["#FF5733", "#33FF57", "#3357FF", "#F333FF"])
        self.title = tk.Label(root, text="नेपाली भ्वाइस असिस्टेन्ट", 
                              font=("Arial", 22, "bold"), fg="white", bg="#000000", pady=10)
        self.title.pack(fill="x")
        self.animate_title()

        # ---- Login Frame ----
        self.frame = tk.Frame(root, bg="white", bd=5, relief="ridge")
        self.frame.place(relx=0.5, rely=0.5, anchor="center", width=350, height=200)

        tk.Label(self.frame, text="Username:", font=("Arial", 12), bg="white").place(x=30, y=40)
        tk.Label(self.frame, text="Password:", font=("Arial", 12), bg="white").place(x=30, y=90)

        self.username_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.username_entry.place(x=130, y=40, width=160)

        self.password_entry = tk.Entry(self.frame, font=("Arial", 12), show="*")
        self.password_entry.place(x=130, y=90, width=160)

        self.login_btn = tk.Button(self.frame, text="Login", bg="green", fg="white", font=("Arial", 12, "bold"),
                                   command=self.check_login)
        self.login_btn.place(x=120, y=140, width=100)

    # ---------- Animation ----------
    def animate_title(self):
        next_color = next(self.colors)
        self.title.config(fg=next_color)
        self.root.after(500, self.animate_title)

    # ---------- Authentication ----------
    def check_login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        # Dummy credentials (replace with DB check if needed)
        if username == "admin" and password == "123":
            messagebox.showinfo("Login Success", "Welcome, " + username)
            self.root.destroy()  # Close login window
            self.open_main_app()
        else:
            messagebox.showerror("Login Failed", "Invalid Username or Password")

    def open_main_app(self):
        root = tk.Tk()
        app.App(root)  # from app.py
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    LoginApp(root)
    root.mainloop()
