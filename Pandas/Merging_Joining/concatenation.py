"""
vertically (row-wise)
horizontally (column-wise)

pd.concate([df1, df2, axis = 0, ignore_index = True])

[df1, df2] = 
axis = 1
"""
#vertically
import pandas as pd

#regin1 
df_Region1 = pd.DataFrame({
    'CustomerId': [1, 2],
    'Nam': ['Gina', 'Raj']
})

#regin2
df_Region2 = pd.DataFrame({
    'CustomerId': [3,4],
    'Nam': ['Sanaya', 'Retix']
})

#concatenate vertically
df_concat = pd.concat([df_Region1, df_Region2], axis = 1, ignore_index = True)
print(df_concat)