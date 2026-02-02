import tkinter as tk
from tkinter import messagebox
from Database import crud, models

class ApplicationForm:
    def __init__(self, parent, user_id, refresh_callback, job=None):
        """
        job = None → Add mode
        job = (id, user_id, company, role, status, deadline, notes) → Edit mode
        """
        self.user_id = user_id
        self.refresh_callback = refresh_callback
        self.job = job

        self.window = tk.Toplevel(parent)
        self.window.title("Edit Application" if job else "Add Application")
        self.window.geometry("400x400")

        # Labels and Inputs
        tk.Label(self.window, text="Company").pack(pady=5)
        self.company_entry = tk.Entry(self.window)
        self.company_entry.pack(pady=5)

        tk.Label(self.window, text="Role").pack(pady=5)
        self.role_entry = tk.Entry(self.window)
        self.role_entry.pack(pady=5)

        tk.Label(self.window, text="Status").pack(pady=5)
        self.status_entry = tk.Entry(self.window)
        self.status_entry.pack(pady=5)

        tk.Label(self.window, text="Deadline (YYYY-MM-DD)").pack(pady=5)
        self.deadline_entry = tk.Entry(self.window)
        self.deadline_entry.pack(pady=5)

        tk.Label(self.window, text="Notes").pack(pady=5)
        self.notes_entry = tk.Entry(self.window)
        self.notes_entry.pack(pady=5)

        # Pre-fill if editing
        if job:
            self.company_entry.insert(0, job[2])
            self.role_entry.insert(0, job[3])
            self.status_entry.insert(0, job[4] if job[4] else "")
            self.deadline_entry.insert(0, job[5] if job[5] else "")
            self.notes_entry.insert(0, job[6] if job[6] else "")

        # Save button
        tk.Button(self.window, text="Save", command=self.save).pack(pady=10)

    def save(self):
        company = self.company_entry.get().strip()
        role = self.role_entry.get().strip()
        status = self.status_entry.get().strip()
        deadline = self.deadline_entry.get().strip()
        notes = self.notes_entry.get().strip()

        if not company or not role:
            messagebox.showerror("Error", "Company and Role are required")
            return

        job_obj = models.JobApplication(company, role, status, deadline, notes,
                                        id=self.job[0] if self.job else None)

        if self.job:  # Edit mode
            crud.update_application(job_obj, self.user_id)
        else:  # Add mode
            crud.add_application(job_obj, self.user_id)

        self.refresh_callback()
        self.window.destroy()
