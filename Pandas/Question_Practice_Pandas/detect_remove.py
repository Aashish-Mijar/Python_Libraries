import pandas as pd

df_dup = pd.DataFrame({
    "Name": ["Ram","Shayam","Ram"],
    "Marks": [90,89,90]
})

# Detect duplicates
print(df_dup.duplicated())

# Remove duplicates
df_dup.drop_duplicates(inplace=True)
print(df_dup)