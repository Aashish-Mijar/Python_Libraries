import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    "Id":[1,2,3,4],
    "Name": ["Ram", "Ramesh", "Romil", "Sital"]
})

df2 = pd.DataFrame({
    "Id": [3,4,5,6,],
    "Marks": [80, 99, 90, 97]
})

# Inner Join

inner = pd.merge(df1, df2, on="Id", how = "inner")
print(inner)