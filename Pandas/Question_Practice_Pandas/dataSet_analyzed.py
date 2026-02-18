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

# Sales by product
print(sales.groupby("Product")["Sales"].sum())

# Highest sale
print("Max sale: ", sales["Sales"].max())

# Pivot summary
print(pd.pivot_table(sales, values="Sales", index="Region", aggfunc="sum"))