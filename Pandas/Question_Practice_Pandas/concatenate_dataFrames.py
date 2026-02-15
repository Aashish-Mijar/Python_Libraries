import pandas as pd

df_a = pd.DataFrame({"A":[1,3], "B":[5,6]})
df_b = pd.DataFrame({"A":[6,8], "B":[7, 2]})

# Vertical concatenation
vertical = pd.concat([df_a, df_b])
print(vertical)

# Horizontal concatenation
horizontal = pd.concat([df_a, df_b], axis = 1)
print(horizontal)