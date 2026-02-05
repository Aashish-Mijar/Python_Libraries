# df["Column Name"].mean()
# df["Column Name"]. sum()
# df["Column Name"]. min()
# df["Column Name"]. max()

import pandas as pd

data ={
    "Name": ["Arun", "Varun", "Karan"],
    "Age": [10, 40, 30],
    "Salary": [10000, 30000, 20000]
}

df = pd.DataFrame(data)

avg_salary = df['Salary'].mean()

print(avg_salary)