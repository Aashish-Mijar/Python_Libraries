import pandas as pd

df_corr = pd.DataFrame({
    "Math":[90,98,87,78],
    "Science":[98,90,89,87],
    "Computer":[90,89,98,99]
})

correlation = df_corr.corr()
print(correlation)