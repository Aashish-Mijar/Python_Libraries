import pandas as pd 

data_dict = {
    "Name": ["Reno","Mauren", "Will"],
    "Age": [20, 23, 22],
    "Marks": [ 94, 98, 97]
}

df = pd.DataFrame(data_dict)
print(df)