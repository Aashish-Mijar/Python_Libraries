import numpy as np

data = np.array([("Ram", 20, 80), ("Shaym", 21, 90)], dtype = [("Name", "U10"), ("Age", "i4"), ("Marks", "f4")])

print(data)

# Access column
print(data["Name"])