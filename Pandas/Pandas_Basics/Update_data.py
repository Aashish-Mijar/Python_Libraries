import pandas as pd

data ={
    "Name": ['Robert', 'Jhon', 'Sunny', 'Clara', 'Mauren'],
    "Age": [20, 34,45,35,45],
    "Salary":[90000, 400000, 560000, 95000, 340000],
    "Performance_Score": [87,89,90,70,80]
}

df = pd.DataFrame(data)
print(df)

# .loc()
# df.loc[row_index, "Column Name" = new_value]

# df.loc[0, 'Salary'] = 120000
# print(df)

df['Salary'] = df['Salary'] * 1.05
print(df)