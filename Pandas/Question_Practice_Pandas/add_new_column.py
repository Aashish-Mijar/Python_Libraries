import pandas as pd

data = {
    "Name":["Ram", "Shyam", "Hari", "Sita"],
    "Class": ["A", "B", "A", "B"],
    "Marks": [ 80, 90, None, 87],
    "Age": [ 20, 21, 22, 21]
}

df = pd.DataFrame(data)
print(df)

df["Result"]= df["Marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")
print(df)

df.drop(columns=["Age"], inplace = True)
print(df)

# Remove row (index 1)
df.drop(index=1, inplace = True)
print(df)

filtered_df = df[df["Marks"]>80]
print(filtered_df)