import pandas as pd

data ={
    "Name": ["Arun", "Varun", "Karan", "Tarun", "Sagar", "Naran"],
    "Age": [30, 40, 30, 35, 30, 24],
    "Salary": [10000, 30000, 20000, 50000, 60000, 35000]
}

df = pd.DataFrame(data)
grouped = df.groupby("Age")["Salary"].sum()
print(grouped)