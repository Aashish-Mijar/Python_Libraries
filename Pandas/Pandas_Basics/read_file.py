import pandas as pd

#  ---- Reading from csv file
# df = pd.read_csv("E:\Files_Semesters\Python\Pandas\sales_data_sample.csv", encoding="latin1")


#  -------- Reading from json file
# df = pd.read_json("E:\Files_Semesters\Python\Pandas\sample_data.json")

# -------- Reading from excel file
df = pd.read_excel("E:\Files_Semesters\Python\Pandas\SampleSuperstore.xlsx")
print(df)

