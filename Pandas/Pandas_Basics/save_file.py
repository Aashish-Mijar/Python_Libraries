import pandas as pd

data = {
    "Name": ['Sita', 'Geeta', 'Hari', "Shyam"],
    "Age": [20,32,34,23],
    "City": ['Waling', 'Butwal', 'Kathmandu', 'Pokhara']
}

df = pd.DataFrame(data)

print(df)

#  save into different file format

# df.to_csv("output.csv", index=False)

# df.to_excel("Output.xlsx", index = False)

df.to_json("Output.json", index = False)
