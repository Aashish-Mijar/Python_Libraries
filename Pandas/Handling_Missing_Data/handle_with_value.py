#fillna()
#fillna(value, inplace = True)
import pandas as pd

data ={
    "Name": ['Robert', None, 'Sunny', 'Clara', 'Mauren'],
    "Age": [20, None,45,35,45],
    "Salary":[90000, None, 560000, 95000, 340000],
    "Performance SCore": [87,None,90,70,80]
}

df = pd.DataFrame(data)
print(df)

print("\nHandle with value")
# df.fillna(0, inplace = True)
df['Age'].fillna(df['Age'].mean(), inplace = True)
df['Salary'].fillna(df['Salary'].mean(), inplace = True)
print(df)