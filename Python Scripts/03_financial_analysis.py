
import pandas as pd

# 1. Load the cleaned dataset
df = pd.read_csv("outputs/cleaned_automotive_data.csv")

# 2. Calculate total financial performance
total_revenue = df["Revenue_INR"].sum()
total_cost = df["Total_Manufacturing_Cost_INR"].sum()
total_profit = df["Operating_Profit_INR"].sum()

# 3. Calculate overall profit margin
profit_margin = (total_profit / total_revenue) * 100

# 4. Display the financial results
print("Total Revenue (INR):", round(total_revenue, 2))
print("Total Manufacturing Cost (INR):", round(total_cost, 2))
print("Total Operating Profit (INR):", round(total_profit, 2))
print("Profit Margin (%):", round(profit_margin, 2))
