class JobApplication:
    def __init__(self, company, role, status, deadline, notes, id=None):
        self.id = id
        self.company = company
        self.role = role
        self.status = status
        self.deadline = deadline
        self.notes = notes
