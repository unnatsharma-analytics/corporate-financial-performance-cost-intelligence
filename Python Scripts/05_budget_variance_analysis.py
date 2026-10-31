
import pandas as pd

# 1. Load the cleaned dataset
df = pd.read_csv("outputs/cleaned_automotive_data.csv")

# 2. Calculate revenue and cost variance
df["Revenue_Variance_INR"] = df["Revenue_INR"] - df["Budget_Revenue_INR"]
df["Cost_Variance_INR"] = df["Total_Manufacturing_Cost_INR"] - df["Budget_Cost_INR"]

# 3. Display total budget variances
print("Total Revenue Variance (INR):", round(df["Revenue_Variance_INR"].sum(), 2))
print("Total Cost Variance (INR):", round(df["Cost_Variance_INR"].sum(), 2))

# 4. Save the results for Tableau
df.to_csv("outputs/budget_variance_analysis.csv", index=False)
