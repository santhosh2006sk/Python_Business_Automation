import pandas as pd
from datetime import datetime

print("Reading file...")

# Read CSV
data = pd.read_csv("data.csv")

# Remove extra spaces from column names
data.columns = data.columns.str.strip()

print("Processing data...")

# If Bonus column missing → create it
if "Bonus" not in data.columns:
    data["Bonus"] = 0

# Calculate total salary
data["Total Salary"] = (data["Days Worked"] * data["Salary per Day"]) + data["Bonus"]

# Add timestamp
data["Generated On"] = datetime.now()

print("Saving report...")

# Save output
data.to_excel("report.xlsx", index=False)

print("✅ Report Generated Successfully!")