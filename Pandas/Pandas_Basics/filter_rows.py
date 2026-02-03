import pandas as pd

data ={
    "Name": ['Robert', 'Jhon', 'Sunny', 'Clara', 'Mauren'],
    "Age": [20, 34,45,35,45],
    "Salary":[90000, 400000, 560000, 95000, 340000],
    "Performance SCore": [87,89,90,70,80]
}

df = pd.DataFrame(data)

high_salary = df[df['Salary']>50000]
print("\nFiltering salary more than 50k")
print(high_salary)

# Filtering rows with 2 or more conditions
filtered = df[(df['Age']>30) | (df['Salary']>90000)]
print("\nFiltering salary based on age")
print(filtered)



