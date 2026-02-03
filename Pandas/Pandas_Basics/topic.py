"""
1- How big is your dataset
2- What are the names of columns

shape and columns
"""
import pandas as pd

data ={
    "Name": ['Robert', 'Jhon', 'Sunny', 'Clara', 'Mauren'],
    "Age": [20, 34,45,35,45],
    "Salary":[90000, 400000, 560000, 95000, 340000],
    "Performance SCore": [87,89,90,70,80]
}

df = pd.DataFrame(data)
print(f'Shape: {df.shape}')
print(f'Column Names: {df.columns}')