from .db_connection import get_connection
from .models import JobApplication

def add_application(job: JobApplication, user_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO applications (user_id, company, role, status, deadline, notes)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (user_id, job.company, job.role, job.status, job.deadline, job.notes))
    conn.commit()
    conn.close()

def get_all_applications(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM applications WHERE user_id=?", (user_id,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_application(job: JobApplication, user_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE applications
        SET company=?, role=?, status=?, deadline=?, notes=?
        WHERE id=? AND user_id=?
    """, (job.company, job.role, job.status, job.deadline, job.notes, job.id, user_id))
    conn.commit()
    conn.close()

def delete_application(app_id: int, user_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM applications WHERE id=? AND user_id=?", (app_id, user_id))
    conn.commit()
    conn.close()
