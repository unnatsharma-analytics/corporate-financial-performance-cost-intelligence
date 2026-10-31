
import pandas as pd
import numpy as np

# 1. Load the cleaned dataset
df = pd.read_csv("outputs/cleaned_automotive_data.csv")

# 2. Calculate potential savings at a 5% cost reduction
cost = df["Total_Manufacturing_Cost_INR"].sum()
savings_rate = np.array([0.05])
potential_savings = cost * savings_rate[0]

# 3. Calculate the estimated cost after savings
estimated_cost = cost - potential_savings

# 4. Display the results
print("Current Manufacturing Cost (INR):", round(cost, 2))
print("Potential Savings at 5% (INR):", round(potential_savings, 2))
print("Estimated Cost After Savings (INR):", round(estimated_cost, 2))

# 5. Save the results for reporting
results = pd.DataFrame({
    "Metric": ["Current Cost", "Potential Savings", "Estimated Cost After Savings"],
    "Amount_INR": [cost, potential_savings, estimated_cost]
})

results.to_csv("outputs/cost_optimization_results.csv", index=False)
