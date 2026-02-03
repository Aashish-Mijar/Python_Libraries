# head() tail()

import pandas as pd
df = pd.read_csv("E:\Files_Semesters\Python\Pandas\sales_data_sample.csv", encoding="latin1")

print("Display 10 rows of first")
print(df.head(10))  # only integers inside head()

print("Display 10 rows of last")
print(df.tail(10))