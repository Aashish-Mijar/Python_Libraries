import pandas as pd

sales = pd.DataFrame({
    "Product": ["A", "B", "A", "C", "B"],
    "Region": ["East", "West", "East", "North", "West"],
    "Sales": [200, 150, 300, 400, 250]
})

# Total sales
print("Total Sales:", sales["Sales"].sum())

# Average Sales
print("Average sales:", sales["Sales"].mean())