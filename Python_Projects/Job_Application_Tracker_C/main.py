from Database.db_connection import init_db
from GUI.animated_login import AnimatedLogin

if __name__ == "__main__":
    init_db()
    app = AnimatedLogin()
    app.run()
