import pandas as pd

data = {
    "Name":["Ram", "Shyam", "Hari", "Sita"],
    "Class": ["A", "B", "A", "B"],
    "Marks": [ 80, 90, None, 87],
    "Age": [ 20, 21, 22, 21]
}

df = pd.DataFrame(data)
print(df)