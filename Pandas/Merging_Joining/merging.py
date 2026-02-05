# pd.merge(df1, df2, on="Column_Name", how="type of join")

import pandas as pd

#customer dataFrame
df_customers = pd.DataFrame({
    'CustomerID': [1,2,3],
    'Name': ['Ramesh', 'Suren', 'Kapil']   
})

#order dataframe
df_orders = pd.DataFrame({
    'CustomerID': [1,2,5],
    'OrderAmount': [250, 450, 350]
})

#merge
# how -inner, outer, left, right
df_merge = pd.merge(df_customers, df_orders, on="CustomerID", how="right")
print("Outer Join")
print(df_merge)