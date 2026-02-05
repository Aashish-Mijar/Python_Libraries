#Sorting data
#SORTING DATA 1 COLUMN sort_values()

#df.sort_values(by="Column_Name", True/False, inplace=True)

import pandas as pd

data ={
    "Name": ["Arun", "Varun", "Karan"],
    "Age": [10, 40, 30],
    "Salary": [10000, 30000, 20000]
}

df = pd.DataFrame(data)

df.sort_values(by="Salary", ascending=False, inplace=True)
print("Sorted Salary by Descending")
print(df)