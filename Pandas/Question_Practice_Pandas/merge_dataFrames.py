import pandas as pd

df1 = pd.DataFrame({
    "Id": [1,3,4],
    "Name": ["Aish", "Shena", "Sarah"]
})

df2 = pd.DataFrame({
    "Id":[1,3,4],
    "Marks": [97,89,99]
})

merged_df = pd.merge(df1, df2, on= "Id")
print(merged_df)