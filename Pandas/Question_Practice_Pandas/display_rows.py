import pandas as pd

df = pd.read_csv("Pandas\Question_Practice_Pandas\example_sales.csv")

print(df.head())
print(df.tail())

rows, columns = df.shape
print("Rows ",rows)
print("Columns ", columns)