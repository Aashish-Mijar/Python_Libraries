import pandas as pd

df = pd.read_csv("Pandas\Question_Practice_Pandas\example_sales.csv")

print(df.head())
print(df.tail())

# Displaying rows and columns number
rows, columns = df.shape
print("Rows ",rows)
print("Columns ", columns)

# Displaying column names and data types

print(df.columns)
print(df.dtypes)