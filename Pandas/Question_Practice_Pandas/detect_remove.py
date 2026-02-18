import pandas as pd

df_dup = pd.DataFrame({
    "Name": ["Ram","Shayam","Ram"],
    "Marks": [90,89,90]
})

# Detect duplicates
print(df_dup.duplicated())