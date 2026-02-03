import pandas as pd

data ={
    "Name": ['Robert', 'Jhon', 'Sunny', 'Clara', 'Mauren'],
    "Age": [20, 34,45,35,45],
    "Salary":[90000, 400000, 560000, 95000, 340000],
    "Performance SCore": [87,89,90,70,80]
}

df = pd.DataFrame(data)

print("Sample data frame")
print(df)

# ----- Describe method
print("Descriptive statistics")
print(df.describe())
