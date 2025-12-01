# importing necessary libraries
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv(r'E:\Files_Semesters\Python\NumPy\NumPyPractice\Practical_dataSet\Employee_data.csv')
print(df.head())

# Checking the missing values
print("Missing values in each column")
print(df.isnull().sum())

# -----------------------------
# 1. Fix missing numeric values
# -----------------------------

# Fill Salary (INR) with mean
df['Salary (INR)'] = df['Salary (INR)'].fillna(df['Salary (INR)'].mean())

# Fill Performance Rating with median
df['Performance Rating'] = df['Performance Rating'].fillna(df['Performance Rating'].median())

# Replace inf values with NaN
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# Fill all numeric columns with their column means
numeric_cols = df.select_dtypes(include=['number']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# --------------------------------
# 2. Fix missing values in text columns
# --------------------------------
text_cols = df.select_dtypes(include=['object']).columns
df[text_cols] = df[text_cols].fillna("Unknown")

# -----------------------------
# 3. Remove duplicate records
# -----------------------------
df.drop_duplicates(inplace=True)

# -----------------------------
# 4. Replace negative salaries
# -----------------------------
df['Salary (INR)'] = np.where(df['Salary (INR)'] < 0,
                              df['Salary (INR)'].mean(),
                              df['Salary (INR)'])

# -----------------------------
# 5. Remove salary outliers (±3 SD)
# -----------------------------
salary_mean = df['Salary (INR)'].mean()
salary_std = df['Salary (INR)'].std()
lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)

df = df[(df['Salary (INR)'] >= lower_bound) & (df['Salary (INR)'] <= upper_bound)]

# -----------------------------
# 6. Save cleaned dataset
# -----------------------------
df.to_csv('Cleaned_employee_data.csv', index=False)

print('Data cleaning completed! Saved as "Cleaned_employee_data.csv"')
