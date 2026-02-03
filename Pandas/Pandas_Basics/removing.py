import pandas as pd

data ={
    "Name": ['Robert', 'Jhon', 'Sunny', 'Clara', 'Mauren'],
    "Age": [20, 34,45,35,45],
    "Salary":[90000, 400000, 560000, 95000, 340000],
    "Performance_Score": [87,89,90,70,80]
}

df = pd.DataFrame(data)
print(df)

# df.drop(columns = ["ColumnName"], inplace = True)

print("Modified Data")
df.drop(columns = ["Performance_Score", "Age"], inplace = True)
print(df)