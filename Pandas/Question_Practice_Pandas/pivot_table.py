import pandas as pd

data = {
    "Name":["Romil", "Jogil", "Harish", "Sigel"],
    "Class": ["A", "B", "A", "B"],
    "Marks": [ 90, 88, 99, 98]
}

df = pd.DataFrame(data)

pivot = pd.pivot_table(df, values="Marks", index="Class", aggfunc="mean")

print(pivot)