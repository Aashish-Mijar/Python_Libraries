import csv
from Database.crud import get_all_applications #

def export_to_csv(filename="applications.csv"):
    apps = get_all_applications()
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Company", "Role", "Status", "Deadline", "Notes"])
        writer.writerows(apps)
