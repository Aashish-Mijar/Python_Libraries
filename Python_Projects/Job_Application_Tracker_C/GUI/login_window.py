from tkinter import messagebox
from Database import auth
from GUI.main_window import JobAppTrackerGUI


def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if auth.verify_user(username, password):
            messagebox.showinfo("Success", "Login Successful!")
            
            # Get user id
            user_id = auth.get_user_id(username)

            self.root.destroy()
            app = JobAppTrackerGUI(user_id)
            app.run()
        else:
            messagebox.showerror("Error", "Invalid username or password")
