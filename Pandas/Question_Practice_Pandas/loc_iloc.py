import pandas as pd

df = pd.DataFrame({
    "Name":["Ram", "Krishna", "Shiva"],
    "Marks":[90,89,99]
},index = ["a", "b", "c"])

# loc -> label-based
print(df.loc["a"])