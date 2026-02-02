from tkinter import Tk, messagebox
from Database import crud
from GUI.forms import ApplicationForm

class JobAppTrackerGUI:
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.root = Tk.Tk()
        self.root.title("Job Application Tracker")
        self.root.geometry("900x500")

        self.create_widgets()
        self.refresh_table()

    def create_widgets(self):
        # Toolbar
        toolbar = Tk.tk.Frame(self.root)
        toolbar.pack(side=Tk.tk.TOP, fill=Tk.tk.X)

        add_btn = Tk.tk.Button(toolbar, text="Add", command=self.add_application)
        add_btn.pack(side=Tk.tk.LEFT, padx=5, pady=5)

        edit_btn = Tk.tk.Button(toolbar, text="Edit", command=self.edit_application)
        edit_btn.pack(side=Tk.tk.LEFT, padx=5, pady=5)

        delete_btn = Tk.tk.Button(toolbar, text="Delete", command=self.delete_application)
        delete_btn.pack(side=Tk.tk.LEFT, padx=5, pady=5)

        # Table
        self.tree = Tk.ttk.Treeview(self.root, columns=("ID", "UserID", "Company", "Role", "Status", "Deadline", "Notes"), show="headings")
        for col in ("ID", "UserID", "Company", "Role", "Status", "Deadline", "Notes"):
            self.tree.heading(col, text=col)
        self.tree.pack(expand=True, fill=Tk.tk.BOTH)

    def refresh_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        apps = crud.get_all_applications(self.user_id)
        for app in apps:
            self.tree.insert("", Tk.tk.END, values=app)

    def add_application(self):
        ApplicationForm(self.root, self.user_id, self.refresh_table)

    def edit_application(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "Select a row to edit")
            return
        item = self.tree.item(selected[0], "values")
        ApplicationForm(self.root, self.user_id, self.refresh_table, job=item)

    def delete_application(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "Select a row to delete")
            return
        item = self.tree.item(selected[0], "values")
        app_id = item[0]
        crud.delete_application(app_id, self.user_id)
        self.refresh_table()
