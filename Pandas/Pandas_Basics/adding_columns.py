import pandas as pd

data ={
    "Name": ['Robert', 'Jhon', 'Sunny', 'Clara', 'Mauren'],
    "Age": [20, 34,45,35,45],
    "Salary":[90000, 400000, 560000, 95000, 340000],
    "Performance SCore": [87,89,90,70,80]
}

df = pd.DataFrame(data)

# square brackets df["Column_Name"]= some_data
print(df)

df["Bonus"] = df['Salary'] * 0.1

print(df)

# Using insert()
# df.insert(loc, "Column_name", some_data)

df.insert(0, "Employee Id", [101, 102, 103,104,105])
print(df)
