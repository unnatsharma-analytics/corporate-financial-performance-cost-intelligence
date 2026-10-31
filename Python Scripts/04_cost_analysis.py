
import pandas as pd

# 1. Load the cleaned dataset
df = pd.read_csv("outputs/cleaned_automotive_data.csv")

# 2. Calculate manufacturing cost by car model
model_cost = df.groupby("Car_Model")["Total_Manufacturing_Cost_INR"].sum()
print("Manufacturing Cost by Car Model:")
print(model_cost.sort_values(ascending=False))

# 3. Calculate manufacturing cost by plant
plant_cost = df.groupby("Plant")["Total_Manufacturing_Cost_INR"].sum()
print("\nManufacturing Cost by Plant:")
print(plant_cost.sort_values(ascending=False))

# 4. Save the analysis results
model_cost.sort_values(ascending=False).to_csv(
    "outputs/cost_by_car_model.csv"
)
plant_cost.sort_values(ascending=False).to_csv(
    "outputs/cost_by_plant.csv"
)
