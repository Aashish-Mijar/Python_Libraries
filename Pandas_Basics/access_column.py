import pandas as pd

data ={
    "Name": ['Robert', 'Jhon', 'Sunny', 'Clara', 'Mauren'],
    "Age": [20, 34,45,35,45],
    "Salary":[90000, 400000, 560000, 95000, 340000],
    "Performance SCore": [87,89,90,70,80]
}

df = pd.DataFrame(data)

print("Sample Dataframe")
print(df)

# Selecting single column
print("\nNames (Single column return series)")
name = df["Name"]
print(name)
# print(name_n)

# selecting multiple columns
subset = df[["Name", "Age"]]
print("\nMultiple Columns")
print(subset)