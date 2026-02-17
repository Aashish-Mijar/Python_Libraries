import pandas as pd

data = {
    "Name":["Romil", "Jogil", "Harish", "Sigel"],
    "Class": ["A", "B", "A", "B"],
    "Marks": [ 90, 88, 99, 98]
}

df = pd.DataFrame(data)

pivot = pd.pivot_table(df, values="Marks", index="Class", aggfunc="mean")

# print(pivot)

# map() for categorical conversion
df["Grade"]= df["Marks"].map(lambda x: "Pass" if x>=40 else "Fail")
# print(df["Grade"])

df["Class"] = df["Class"].replace({"A":"First", "B":"Second"})
print(df["Class"])

# map() -> Seris only
df["Marks_double"] = df["Marks"].map(lambda x: x*2)
# print(df["Marks_double"])

# apply() -> Series or DataFrame
df["Marks_Square"] = df["Marks"].apply(lambda x: x ** 2)
print(df["Marks_Square"])