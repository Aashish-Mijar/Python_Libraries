import pandas as pd

df_dates = pd.DataFrame({
    "Date": ["2026-01-01", "2026-02-15", "2026-03-10"]
})

df_dates["Date"] = pd.to_datetime(df_dates["Date"])

# Extract year
df_dates["Year"] = df_dates["Date"].dt.year

# Extract month
df_dates["Month"] = df_dates["Date"].dt.month

# Extract day
df_dates["Day"] = df_dates["Date"].dt.day

print(df_dates)