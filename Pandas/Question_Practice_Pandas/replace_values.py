import pandas as pd

data = {
    "Name":["Ram", "Shyam", "Hari", "Sita"],
    "Class": ["A", "B", "A", "B"],
    "Marks": [ 80, 90, None, 87],
    "Age": [ 20, 21, 22, 21]
}

df = pd.DataFrame(data)

# Replace missing values with mean and median

# df["Marks"].fillna(df["Marks"].mean(), inplace=True)

# df["Marks"].fillna(df["Marks"].median(), inplace=True)

# Sort by Marks (ascending)
# print(df.sort_values(by = "Marks"))

# Sort by Class then Marks (descending)
print(df.sort_values(by=["Class", "Marks"], ascending=[True, False]))


# print(df)

# Mean marks by class
print(df.groupby("Class")["Marks"].mean())