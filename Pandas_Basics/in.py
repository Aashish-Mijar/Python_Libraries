import pandas as pd

df = pd.read_json("E:\Files_Semesters\Python\Pandas\sample_data.json")

print("Displaying the info of data set")
print(df.info())