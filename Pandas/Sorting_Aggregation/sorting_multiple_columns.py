import pandas as pd

data ={
    "Name": ["Arun", "Varun", "Karan"],
    "Age": [10, 40, 30],
    "Salary": [10000, 30000, 20000]
}

df = pd.DataFrame(data)

df.sort_values(by=["Age", "Salary"], ascending=[True, False], inplace=True)
print("Sorted Age by Descending")
print(df)