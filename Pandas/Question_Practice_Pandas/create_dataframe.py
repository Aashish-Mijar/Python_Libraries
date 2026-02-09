import pandas as pd 

data_dict = {
    "Name": ["Reno","Mauren", "Will"],
    "Age": [20, 23, 22],
    "Marks": [ 94, 98, 97]
}

df = pd.DataFrame(data_dict)
print(df)

# Rename Columns dataframe
df.rename(columns={
    "Name":"Students_Name",
    "Marks":"Total_Marks"
}, inplace=True)

print(df)

# Check missing values
print(df.isnull())

# Count missing values
print(df.isnull().sum())