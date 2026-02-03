# Giving estimated value 
"""
10
20
NaN  #Could be 30 
40 
50


1 - preserver data integrity
2 - smooth trends
3 - avoid data loss

interpolate()
"""
import pandas as pd

data ={
    "Name": ['Robert', "John", 'Sunny', 'Clara', 'Mauren'],
    "Age": [20, None,45,35,45],
    "Salary":[90000, None, 560000, 95000, 340000],
    "Performance SCore": [87,None,90,70,80]
}

df = pd.DataFrame(data)
print(df)

# linear. polynomial, time
df.interpolate(method = "linear", axis = 0, inplace = True)
print(df)